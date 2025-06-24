import argparse
import csv
import os.path

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
def save_expenses():
    with open(FILE, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows()

# Parse CLI Arguments
def parse_cli_args():
    # Create the main parser
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    # Create subparsers for different commands
    subparser = parser.add_subparsers(dest="command")
    # Command: add
    add_parser = subparser.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", type=str, required=True, help="Expense description")
    add_parser.add_argument("--category", type=str, required=True, help="Expense category")
    # Command: update
    update_parser = subparser.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", type=int, required=True, help="Expense ID")
    update_parser.add_argument("--description", type=str, required=True, help="Expense description")
    update_parser.add_argument("--category", type=str, required=False, help="Expense category")
    # Command: delete
    delete_parser = subparser.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID")
    # Command: list
    list_parser = subparser.add_parser("list", help="View all expenses")
    list_parser.add_argument("--month", type=str, required=False, choices=["January", "February", "March", "April", "May", "June",
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
        return 1
    max_id = max(expenses.get("id", 0) for expense in expenses)
    return  max_id + 1

# Handle Commands
def handle_commands(args):
    match args.command:
        case "add":
            print(args.command)
        case "update":
            print(args.command)
        case "delete":
            print(args.command)
        case "list":
            print(args.command)
        case "summary":
            print(args.command)
        case _:
            print("Invalid command")

def main():
    args = parse_cli_args()
    initialize_csv()
    handle_commands(args)

main()