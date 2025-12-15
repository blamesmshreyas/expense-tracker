import csv
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    file = open(FILE_NAME, "a", newline="")
    file.close()

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    file = open(FILE_NAME, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([date, category, amount, description])
    file.close()

    print("Expense added successfully!")

def show_expenses():
    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    print("\nDate       Category    Amount    Description")
    print("-" * 45)

    for row in reader:
        print(row[0], " ", row[1], "   ₹", row[2], "  ", row[3])

    file.close()

def show_graph():
    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    category_totals = {}

    for row in reader:
        category = row[1]
        amount = float(row[2])

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    file.close()

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.bar(categories, amounts)
    plt.title("Expense Tracker Graph")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def main():
    initialize_file()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Show Graph")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_graph()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()

