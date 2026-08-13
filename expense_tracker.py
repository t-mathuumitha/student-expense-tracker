
import os

FILENAME = "expenses.txt"


def load_expenses():
    expenses = []

    if not os.path.exists(FILENAME):
        return expenses

    file = open(FILENAME, "r")

    for line in file:
        line = line.strip()

        if line == "":
            continue

        parts = line.split("|")

        date = parts[0]
        category = parts[1]
        description = parts[2]
        amount = parts[3]

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": float(amount)
        }

        expenses.append(expense)

    file.close()

    return expenses


def save_expenses(expenses):
    file = open(FILENAME, "w")

    for expense in expenses:
        line = (
            expense["date"] + "|" +
            expense["category"] + "|" +
            expense["description"] + "|" +
            str(expense["amount"]) + "\n"
        )

        file.write(line)

    file.close()


def add_expense(expenses):
    date = input("Date (e.g. 2026-08-14): ")

    category = input("Category (Food, Transport, Books, etc): ")
    category = category.strip().title()

    description = input("What was it for? ")

    amount = input("Amount: ")

    while True:
        try:
            amount = float(amount)
            break
        except ValueError:
            print("Please enter a valid amount.")
            amount = input("Amount: ")

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added.\n")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return

    print("\nDate         Category         Description         Amount")
    print("---------------------------------------------------------")

    for expense in expenses:
        print(
            expense["date"],
            " ",
            expense["category"],
            " ",
            expense["description"],
            " ",
            expense["amount"]
        )

    print()


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def spending_by_category(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]

        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]

    return totals


def show_category_breakdown(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return

    totals = spending_by_category(expenses)

    print()

    for category in totals:
        print(category, "-", round(totals[category], 2))

    print()


def show_menu():
    print("--------------------------")
    print("STUDENT EXPENSE TRACKER")
    print("--------------------------")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Total spending")
    print("4. Spending by category")
    print("5. Quit")


def main():
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input("Pick an option: ")
        choice = choice.strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print("\nTotal spending:", round(total, 2), "\n")

        elif choice == "4":
            show_category_breakdown(expenses)

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid option. Please try again.\n")


main()
