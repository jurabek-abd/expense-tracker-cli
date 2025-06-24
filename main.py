import argparse
import csv
import os.path
from datetime import datetime
import pprint

FILE = "expenses.csv"
FIELDS = ["id", "description", "amount", "month", "category"]


# Initialize CSV
def initialize_csv():
    if not os.path.exists(FILE):
        with open(FILE, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


# Load CSV
def load_expenses():
    if not os.path.exists(FILE):
        return []

    with open(FILE, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)


# Save CSV
def save_expenses(expenses):
    with open(FILE, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


# Parse CLI Arguments
def parse_cli_args():
    # Create the main parser
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    # Create subparsers for different commands
    subparser = parser.add_subparsers(dest="command")
    # Command: add
    add_parser = subparser.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", type=str, required=True, help="Expense description")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")
    add_parser.add_argument("--category", type=str, required=True, help="Expense category")
    # Command: update
    update_parser = subparser.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", type=int, required=True, help="Expense ID")
    update_parser.add_argument("--description", type=str, required=True, help="Expense description")
    update_parser.add_argument("--amount", type=float, required=True, help="Expense amount")
    update_parser.add_argument("--category", type=str, required=True, help="Expense category")
    # Command: delete
    delete_parser = subparser.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID")
    # Command: list
    list_parser = subparser.add_parser("list", help="View all expenses")
    list_parser.add_argument("--month", type=str, required=False,
                             choices=["January", "February", "March", "April", "May", "June",
                                      "July", "August", "September", "October", "November",
                                      "December"], help="Filter expenses by month")
    list_parser.add_argument("--category", type=str, required=False, help="View all expenses by category")
    # Command: summary
    summary_parser = subparser.add_parser("summary", help="View summary")
    summary_parser.add_argument("--month", type=str, choices=["January", "February", "March", "April", "May", "June",
                                                              "July", "August", "September", "October", "November",
                                                              "December"], help="Filter summary by month")
    summary_parser.add_argument("--category", type=str, required=False, help="View summary by category")

    return parser.parse_args()


# Generate ID
def generate_expense_id(expenses):
    if not expenses:
        return 1  # if file is empty, start at 1
    max_id = max(int(exp["id"]) for exp in expenses)
    return max_id + 1


# Handle: add
def handle_add(description, category, amount):
    expenses = load_expenses()
    expense_id = generate_expense_id(expenses)

    if amount < 1:
        return print("Amount cannot be lower than 1")

    expenses.append({
        "id": expense_id,
        "description": description,
        "category": category,
        "amount": amount,
        "month": datetime.now().strftime("%B")
    })

    save_expenses(expenses)
    print(f"Expense added (ID-{expense_id})")


# Handle: update
def handle_update(expense_id, description, category, amount):
    expenses = load_expenses()

    if not any(exp["id"] == str(expense_id) for exp in expenses):
        return print("Invalid ID")

    if amount < 1:
        return print("Amount cannot be lower than 1")

    for expense in expenses:
        if int(expense["id"]) == expense_id:
            expense["description"] = description
            expense["category"] = category
            expense["amount"] = amount
            break

    save_expenses(expenses)
    print(f"Expense updated (ID-{expense_id})")


# Handle: delete
def handle_delete(expense_id):
    expenses = load_expenses()

    if not any(exp["id"] == str(expense_id) for exp in expenses):
        return print("Invalid ID")

    for expense in expenses:
        if int(expense["id"]) == expense_id:
            expenses.remove(expense)
            break

    save_expenses(expenses)
    print(f"Expense deleted (ID-{expense_id})")


# Handle: list
def print_expenses_table(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':<4} {'Month':<10} {'Description':<20} {'Category':<15} {'Amount':>8}")
    print("-" * 65)
    for e in expenses:
        print(f"{e['id']:<4} {e['month']:<10} {e['description']:<20} {e['category']:<15} ${float(e['amount']):>7.2f}")

def filter_expenses(expenses, month, category):

    if month and category:
        filtered = [e for e in expenses if
                    e["month"].lower() == month.lower() and e["category"].lower() == category.lower()]
    elif month:
        filtered = [e for e in expenses if e["month"].lower() == month.lower()]
    elif category:
        filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    else:
        filtered = expenses

    return filtered
def handle_list(month, category):
    expenses = load_expenses()

    print_expenses_table(filter_expenses(expenses, month, category))
# Handle: summary
def handle_summary(month, category):
    expenses = load_expenses()

    print(f"Total {"for " + month if month else ""}{" and " if month and category else ""}{"for " + category + " category" if category else ""}: {sum(float(e["amount"]) for e in filter_expenses(expenses, month, category))}")

# Handle Commands
def handle_commands(args):
    match args.command:
        case "add":
            handle_add(args.description, args.category, args.amount)
        case "update":
            handle_update(args.id, args.description, args.category, args.amount)
        case "delete":
            handle_delete(args.id)
        case "list":
            handle_list(args.month, args.category)
        case "summary":
            handle_summary(args.month, args.category)
        case _:
            print("Invalid command")


def main():
    args = parse_cli_args()
    initialize_csv()
    handle_commands(args)


main()
