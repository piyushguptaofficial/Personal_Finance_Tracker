# This file containe the core business logic of the application.
from storage import read_transactions


def all_transactions():
    return read_transactions()


def calculate_balance():
    income = 0
    expense = 0

    for row in read_transactions():
        if row[1] == "Income":
            income += float(row[3])
        elif row[1] == "Expense":
            expense += float(row[3])

    return income, expense, income - expense


def category_summary():
    summary = {}

    for row in read_transactions():
        if row[1] == "Expense":
            category = row[2]
            amount = float(row[3])
            summary[category] = summary.get(category, 0) + amount

    return summary


def monthly_transactions(month):
    result = []

    for row in read_transactions():
        if row[0].split("-")[1] == month.zfill(2):
            result.append(row)

    return result
