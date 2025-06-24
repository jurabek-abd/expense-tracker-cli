# 💰 Expense Tracker CLI

A simple command-line application to manage your personal expenses. Easily add, update, delete, and list your expenses — all stored in a local CSV file.

> 📌 Project inspired by [roadmap.sh](https://roadmap.sh/projects/expense-tracker)

---

## 🚀 Features

- ➕ Add expenses with a description, amount, and category
- ✏️ Update existing expenses by ID
- ❌ Delete expenses by ID
- 📋 List all expenses, or filter by month and/or category
- 📊 View a summary of total expenses, optionally filtered
- 💾 Data is saved persistently in `expenses.csv`

---

## ⚙️ How to Use

### 📌 Add an Expense

```bash
python main.py add --description "Lunch" --amount 15.5 --category "Food"
```

### ✏️ Update an Expense

```bash
python main.py update --id 1 --description "Dinner" --amount 20 --category "Food"
```

### ❌ Delete an Expense

```bash
python main.py delete --id 1
```

### 📋 List All Expenses

```bash
python main.py list
```

#### Optional Filters

```bash
python main.py list --month July
python main.py list --category Food
python main.py list --month July --category Food
```

### 📊 View Summary

```bash
python main.py summary
```

#### Optional Filters

```bash
python main.py summary --month July
python main.py summary --category Food
```

---

## 🧾 Sample Output

```
ID   Month      Description          Category        Amount
-------------------------------------------------------------
1    June       Grocery Shopping     Food            $45.00
2    June       Taxi Ride            Transport       $10.00

Total for June: $55.00
```

---

## 📁 Data Format

All expenses are saved in a CSV file with the following columns:

- `id`: Unique integer ID
- `description`: What the expense is for
- `amount`: How much was spent
- `month`: Month (automatically set to current)
- `category`: Expense category (e.g., Food, Rent, Travel)

---

## 🧠 Skills Practiced

- Python `argparse` CLI parsing
- File handling with CSV module
- Data filtering and summarization
- Modular function design
- Real-world CLI app structure

---

## 👤 Author

**Jurabek**  
High school student and aspiring **AI Chatbot Developer**.  
Passionate about building real-world Python projects from scratch.

