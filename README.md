# Personal Finance Tracker 🧾

A GUI-based Personal Finance Tracker built using **Python** and **Tkinter**.  
This application helps users record income and expenses, analyze spending patterns, and visualize expenses using charts.

---

## 📌 Features

- Add Income and Expense transactions
- View all transactions
- Calculate total income, total expense, and balance
- Category-wise expense summary
- Monthly transaction filter
- Expense distribution pie chart
- Reset UI and reset all stored data (with confirmation)
- Persistent storage using CSV files

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- CSV (Data storage)
- Matplotlib (Charts)
- Virtual Environment (venv)

---

## 📂 Project Structure

Personal_Finance_Tracker/
│
├── main.py # GUI and event handling
├── logic.py # Business logic and calculations
├── storage.py # File handling (CSV)
├── charts.py # Data visualization
│
├── data/
│ └── transactions.csv
│
├── venv/ # Virtual environment (not pushed to GitHub)
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Personal_Finance_Tracker.git
cd Personal_Finance_Tracker

# Create & activate virtural environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install matplotlib

# Run this application
python main.py


📊 Expense Chart

The application generates a pie chart to visualize expense distribution across categories.

# 🧠 Learning Outcomes

GUI programming using Tkinter

File handling with CSV

Modular programming in Python

Data validation and normalization

Basic data visualization

Use of virtual environments

Version control with Git & GitHub



✅ This README is:
- GitHub-ready
- Teacher-friendly
- Viva-safe
- Professional

---

## 🧹 PART 1.5: IMPORTANT – Create `.gitignore`

You **MUST NOT** push `venv/` to GitHub.

Create a file named **`.gitignore`** and add:

```gitignore
venv/
__pycache__/
*.pyc
data/transactions.csv
