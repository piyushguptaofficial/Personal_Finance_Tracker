# This file (Charts) helps visualize financial data, expense distribution, and trends for better understanding.
import csv
import matplotlib.pyplot as plt
from storage import FILE_PATH


def expense_pie_chart():
    categories = {}

    with open(FILE_PATH, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == "Expense":
                categories[row[2]] = categories.get(row[2], 0) + float(row[3])

    if not categories:
        return False

    plt.figure(figsize=(6, 6))
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()
    return True
