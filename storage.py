# This file is used for storing transaction data in a CSV file.
import csv
import os
from datetime import date

FILE_PATH = "data/transactions.csv"
os.makedirs("data", exist_ok=True)


def save_transaction(t_type, category, amount):
    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date.today(), t_type, category, amount])


def read_transactions():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        return list(csv.reader(file))

def clear_all_transactions():
    open(FILE_PATH, 'w').close()