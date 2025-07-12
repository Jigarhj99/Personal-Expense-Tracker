
# 💰 Personal Expense Tracker (Tkinter GUI)

A desktop application built using **Python Tkinter** that allows users to track their daily expenses. This app stores data in a CSV file and provides options to add, view, and filter expenses by category or date.

---

## 🖥️ Features

- ➕ Add expense entries with:
  - Amount
  - Category
  - Optional Note
  - Auto-filled Date (Today's Date)
- 🔍 Filter expenses by:
  - **Category**
  - **Date**
- 📊 View all records in a tabular format (TreeView).
- 💸 Display total amount spent.
- 🧹 Reset filters to show all records.
- 🗂 Stores all data in `my_expenses.csv` file.

---

## 🖼️ GUI Preview

<img width="866" height="781" alt="image" src="https://github.com/user-attachments/assets/943d7cbd-dfeb-4eff-8369-f4d2831da2f2" />

---

## 🧾 How It Works

- The app creates a `my_expenses.csv` file if it doesn't already exist.
- Each time you add an expense, it's saved with the current date in the CSV.
- You can search by **category name** (e.g. "food") or **date** (e.g. "2025-07-11") to filter the table.
- The total amount spent (based on visible records) is shown at the bottom.

---

