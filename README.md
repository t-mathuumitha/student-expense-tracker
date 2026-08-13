# Student Expense Tracker

A simple Python console application for recording and managing daily expenses. The program saves expense records to a text file so the data can be loaded again when the program is restarted.

## Features

* Add daily expenses
* Enter date, category, description, and amount
* View all recorded expenses
* Calculate total spending
* View spending by category
* Save expenses to a text file
* Load saved expenses when the program starts
* Handle invalid amount input

## Technologies Used

* Python
* File Handling
* Lists
* Dictionaries
* Functions
* Exception Handling
* Basic Data Processing

## How It Works

When the program starts, it checks whether an `expenses.txt` file exists. If the file exists, previously saved expenses are loaded.

Users can then choose from the following options:

```text
1. Add expense
2. View all expenses
3. Total spending
4. Spending by category
5. Quit
```

When a new expense is added, it is stored in memory and saved to the text file.

## Example

```text
--------------------------
STUDENT EXPENSE TRACKER
--------------------------
1. Add expense
2. View all expenses
3. Total spending
4. Spending by category
5. Quit

Pick an option: 1

Date (e.g. 2026-08-14): 2026-08-14
Category (Food, Transport, Books, etc): Food
What was it for? Lunch
Amount: 450

Expense added.
```

## File Storage

The program uses a text file called:

```text
expenses.txt
```

Each expense is stored using the following format:

```text
date|category|description|amount
```

Example:

```text
2026-08-14|Food|Lunch|450.0
```

> **Note:** `expenses.txt` is intended for local expense data. Avoid uploading personal spending information to a public repository.

## Project Structure

```text
student-expense-tracker/
│
├── expense_tracker.py
├── README.md
└── .gitignore
```

## What I Learned

This project helped me practice Python fundamentals, including:

* Working with functions
* Using lists and dictionaries
* Reading and writing text files
* Handling user input
* Using `try` and `except`
* Processing and summarizing data
* Building a simple menu-driven application

## Future Improvements

Some features I may add in the future:

* Delete an expense
* Edit an existing expense
* Search expenses by date or category
* Monthly spending summaries
* Budget tracking
* Export expenses to CSV
* A graphical user interface

## Author

**Mathuumitha Thevarajah**

GitHub: [t-mathuumitha](https://github.com/t-mathuumitha)

---

If you find this project useful, feel free to explore the repository and follow my GitHub profile.
