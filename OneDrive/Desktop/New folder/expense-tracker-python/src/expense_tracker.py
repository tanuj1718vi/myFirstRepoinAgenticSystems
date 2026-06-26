import json
import os

FILE_NAME = "expenses.json"

# ---------------- LOAD DATA ----------------
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# ---------------- SAVE DATA ----------------
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ---------------- ADD EXPENSE ----------------
def add_expense(data):
    category = input("Category (Food/Travel/Shopping/Other): ")
    amount = float(input("Amount: "))
    note = input("Note: ")

    expense = {
        "category": category,
        "amount": amount,
        "note": note
    }

    data.append(expense)
    save_data(data)
    print("Expense added!\n")

# ---------------- VIEW EXPENSES ----------------
def view_expenses(data):
    if not data:
        print("No expenses found.\n")
        return

    print("\n===== ALL EXPENSES =====")
    for i, exp in enumerate(data, start=1):
     print(f"{i}. Category: {exp['category']} | Amount: ₹{exp['amount']} | Note: {exp['note']}")

# ---------------- TOTAL EXPENSE ----------------
def total_expense(data):
    total = sum(e["amount"] for e in data)
    print("\nTotal Expense:", total, "\n")

# ---------------- CATEGORY WISE ----------------
def category_wise(data):
    categories = {}

    for e in data:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]

    print("\n===== CATEGORY WISE EXPENSE =====")
    for k, v in categories.items():
        print(k, ":", v)
    print()

# ---------------- BUDGET CHECK ----------------
def budget_check(data):
    budget = float(input("Enter monthly budget: "))
    total = sum(e["amount"] for e in data)

    print("\nBudget:", budget)
    print("Spent:", total)

    if total > budget:
        print("❌ Budget exceeded!")
    else:
        print("✅ Within budget")

# ---------------- MENU ----------------
def menu():
    data = load_data()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Wise Report")
        print("5. Budget Check")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            total_expense(data)
        elif choice == "4":
            category_wise(data)
        elif choice == "5":
            budget_check(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

menu()