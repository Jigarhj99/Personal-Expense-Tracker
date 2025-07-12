import csv
import os
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

# File configuration
FILENAME = 'my_expenses.csv'
COLUMNS = ['Date', 'Amount', 'Category', 'Note']

# Create CSV file with headers if it doesn't exist
def initialize_csv_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS)

# Function to add a new expense
def add_expense():
    try:
        amount = float(entry_amount.get().strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        return

    category = entry_category.get().strip()
    note = entry_note.get().strip()
    date_today = datetime.now().strftime('%Y-%m-%d')

    if category == "":
        messagebox.showerror("Missing Input", "Category cannot be empty.")
        return

    # Write the expense to CSV file
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_today, amount, category, note])

    # Clear input fields
    entry_amount.delete(0, END)
    entry_category.delete(0, END)
    entry_note.delete(0, END)

    # Update the table
    load_expenses()

    messagebox.showinfo("Success", "Expense added successfully!")

# Function to display expenses in the table
def load_expenses(filtered_data=None):
    for item in expense_table.get_children():
        expense_table.delete(item)

    total = 0

    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers

            for row in reader:
                if filtered_data and row not in filtered_data:
                    continue
                if len(row) == 4:
                    expense_table.insert('', END, values=row)
                    try:
                        total += float(row[1])
                    except ValueError:
                        continue

        total_label.config(text=f"Total Spent: ₹{total:.2f}")

    except FileNotFoundError:
        messagebox.showwarning("Warning", "Expense file not found.")

# Function to filter expenses
def filter_expenses():
    keyword = entry_filter.get().strip().lower()
    filter_type = filter_option.get().strip()

    if keyword == "":
        messagebox.showwarning("Missing Input", "Please enter filter keyword.")
        return

    matching_rows = []

    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if filter_type == "Category" and row[2].strip().lower() == keyword:
                    matching_rows.append(row)
                elif filter_type == "Date" and row[0].strip() == keyword:
                    matching_rows.append(row)

        load_expenses(filtered_data=matching_rows)

    except FileNotFoundError:
        messagebox.showwarning("File Error", "CSV file not found.")

# Function to reset filter and show all expenses
def reset_filter():
    entry_filter.delete(0, END)
    load_expenses()

# --------------------- GUI SETUP --------------------- #
# Initialize the file
initialize_csv_file()

# Create the main window
window = Tk()
window.title("Personal Expense Tracker")
window.geometry("700x600")
window.resizable(False, False)

# ----- Entry Section ----- #
frame_entry = Frame(window, padx=10, pady=10)
frame_entry.pack(fill=X)

Label(frame_entry, text="Amount (₹):").grid(row=0, column=0, padx=5, pady=5)
entry_amount = Entry(frame_entry, width=15)
entry_amount.grid(row=0, column=1)

Label(frame_entry, text="Category:").grid(row=0, column=2, padx=5)
entry_category = Entry(frame_entry, width=15)
entry_category.grid(row=0, column=3)

Label(frame_entry, text="Note:").grid(row=0, column=4, padx=5)
entry_note = Entry(frame_entry, width=15)
entry_note.grid(row=0, column=5)

Button(frame_entry, text="Add Expense", command=add_expense, bg="green", fg="white").grid(row=0, column=6, padx=10)

# ----- Filter Section ----- #
frame_filter = Frame(window, padx=10, pady=5)
frame_filter.pack(fill=X)

filter_option = StringVar(value="Category")
Label(frame_filter, text="Filter by:").pack(side=LEFT)
OptionMenu(frame_filter, filter_option, "Category", "Date").pack(side=LEFT, padx=5)

entry_filter = Entry(frame_filter, width=20)
entry_filter.pack(side=LEFT, padx=5)

Button(frame_filter, text="Search", command=filter_expenses).pack(side=LEFT, padx=5)
Button(frame_filter, text="Reset", command=reset_filter).pack(side=LEFT)

# ----- Table Section ----- #
frame_table = Frame(window, padx=10, pady=10)
frame_table.pack(fill=BOTH, expand=True)

expense_table = ttk.Treeview(frame_table, columns=COLUMNS, show='headings')
for col in COLUMNS:
    expense_table.heading(col, text=col)
    expense_table.column(col, width=150)

expense_table.pack(fill=BOTH, expand=True)

# ----- Total Label ----- #
total_label = Label(window, text="Total Spent: ₹0.00", font=("Arial", 12, "bold"), pady=10)
total_label.pack()

# Load all data when program starts
load_expenses()

# Run the GUI
window.mainloop()
