# Simple Python & SQL Inventory Tracker

A lightweight, terminal-based application built to understand the fundamentals of integrating Python with a relational database. This system allows a user to manage and log store room inventory data seamlessly using localized database storage.

## 🚀 Features
* **Interactive Menu:** Simple console-based interface for easy navigation.
* **Persistent Storage:** Data is saved securely in a local database file, meaning records are kept even after the application closes.
* **Database Operations:** Demonstrates core CRUD concepts (Creating tables, Inserting records, and Fetching data).

## 🛠️ Tech Stack & Concepts Used
* **Language:** Python 3
* **Database Engine:** SQLite (Built-in relational database helper)
* **SQL Queries:** `CREATE TABLE`, `INSERT INTO`, `SELECT`
* **Python Concepts:** `while` loops, conditional logic (`if-elif-else`), user `input()` functions, and iterators (`for` loop).

## 📊 How the Architecture Works
The application acts as a middleman between the user and the storage file:
User Input ➔ Python Script ➔ SQL Query ➔ SQLite Database (.db file)

## 💻 How to Run This Project

1. **Clone or Download the Repository:**
   Download the `inventory.py` file to your computer.

2. **Open Terminal / Command Prompt:**
   Navigate to the folder where you saved the file.

3. **Run the Script:**
   Execute the following command in your terminal:
   ```bash
   python inventory.py
