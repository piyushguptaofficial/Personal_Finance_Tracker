# This File is for the main entry point of the financial tracking application. GUI + Controller 
import tkinter as tk
from tkinter import messagebox

from storage import save_transaction, clear_all_transactions
from logic import calculate_balance, category_summary, monthly_transactions, all_transactions
from charts import expense_pie_chart


def all_transactions():
    t_type = type_var.get()
    category = category_entry.get().strip()
    amount = amount_entry.get().strip()

    # ONLY validate fields needed for adding transaction
    if category == "" or amount == "":
        messagebox.showerror("Error", "Category and Amount are required")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive amount")
        return

    save_transaction(t_type, category, amount)
    messagebox.showinfo("Success", "Transaction added successfully")

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


    save_transaction(t_type, category, amount)
    messagebox.showinfo("Success", "Transaction added")

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def show_transactions():
    output.delete(1.0, tk.END)

    transactions = all_transactions()

    if not transactions:
        output.insert(tk.END, "No transactions found.\n")
        return

    for row in transactions:
        output.insert(
            tk.END,
            f"{row[0]} | {row[1]} | {row[2]} | ₹{row[3]}\n"
        )


def show_balance():
    income, expense, balance = calculate_balance()
    messagebox.showinfo(
        "Balance",
        f"Income: ₹{income}\nExpense: ₹{expense}\nBalance: ₹{balance}"
    )


def show_category_summary():
    output.delete(1.0, tk.END)
    summary = category_summary()
    output.insert(tk.END, "Category-wise Expense Summary\n\n")
    for k, v in summary.items():
        output.insert(tk.END, f"{k} : ₹{v}\n")


def show_chart():
    if not expense_pie_chart():
        messagebox.showinfo("Chart", "No expense data available")


def reset_ui():
    type_var.set("Income")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    output.delete(1.0, tk.END)

def reset_all_data():
    confirm = messagebox.askyesno(
        "Confirm Reset",
        "This will delete ALL transactions.\nAre you sure?"
    )

    if confirm:
        clear_all_transactions()
        reset_ui()
        messagebox.showinfo("Reset", "All data has been cleared")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("1500x1200")
root.resizable(False, False)

tk.Label(root, text="Personal Finance Tracker", font=("Arial", 16, "bold")).pack(pady=10)

type_var = tk.StringVar(value="Income")
tk.Label(root, text="Transaction Type").pack()
tk.OptionMenu(root, type_var, "Income", "Expense").pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Month (MM - optional)").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Button(root, text="Add Transaction", command=all_transactions).pack(pady=8)
tk.Button(root, text="Show Balance", command=show_balance).pack()
tk.Button(root, text="Category Summary", command=show_category_summary).pack()
# tk.Button(root, text="Show Transactions", command=show_transactions).pack()
tk.Button(root, text="Expense Chart", command=show_chart).pack(pady=5)
tk.Button(root, text="Reset", command=reset_ui).pack(pady=5)
tk.Button(
    root,
    text="Reset All Data",
    command=reset_all_data,
    fg="red"
).pack(pady=5)


output = tk.Text(root, height=12, width=65)
output.pack(pady=10)

root.mainloop()
