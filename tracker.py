import json
import os

FILE = "expenses.json"

# ---------- FILE HANDLING ----------
def load_data():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- CORE FUNCTIONS ----------
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc.): ")

    data = load_data()
    data.append({
        "name": name,
        "amount": amount,
        "category": category
    })

    save_data(data)
    print("✅ Expense added successfully!")


def show_expenses():
    data = load_data()
    
    if not data:
        print("No expenses found.")
        return

    print("\n📋 All Expenses:")
    for i, exp in enumerate(data):
        print(f"{i}. {exp['name']} | Rs {exp['amount']} | {exp['category']}")


def delete_expense():
    data = load_data()
    show_expenses()

    try:
        index = int(input("Enter index to delete: "))
        removed = data.pop(index)
        save_data(data)
        print(f"❌ Deleted: {removed['name']}")
    except:
        print("Invalid index!")


def update_expense():
    data = load_data()
    show_expenses()

    try:
        index = int(input("Enter index to update: "))
        
        name = input("New name: ")
        amount = float(input("New amount: "))
        category = input("New category: ")

        data[index] = {
            "name": name,
            "amount": amount,
            "category": category
        }

        save_data(data)
        print("🔄 Expense updated!")
    except:
        print("Invalid input!")


def filter_by_category():
    data = load_data()
    category = input("Enter category to filter: ")

    filtered = [exp for exp in data if exp["category"].lower() == category.lower()]

    if not filtered:
        print("No expenses found in this category.")
        return

    print(f"\n📂 {category} Expenses:")
    for exp in filtered:
        print(f"{exp['name']} | Rs {exp['amount']}")


# ---------- MENU ----------
def menu():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            filter_by_category()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!")


# ---------- RUN ----------
menu()