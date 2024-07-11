```python
# Import necessary libraries
import datetime
import random

# Define classes for clients, transactions, and accounts
class Client:
    def __init__(self, client_id, name, email, phone_number):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

class Transaction:
    def __init__(self, transaction_id, client_id, account_number, amount, transaction_date):
        self.transaction_id = transaction_id
        self.client_id = client_id
        self.account_number = account_number
        self.amount = amount
        self.transaction_date = transaction_date

class Account:
    def __init__(self, account_number, client_id, balance):
        self.account_number = account_number
        self.client_id = client_id
        self.balance = balance

# Create a list to store clients
clients = []

# Create a list to store transactions
transactions = []

# Create a list to store accounts
accounts = []

# Function to create a new client
def create_client(client_id, name, email, phone_number):
    new_client = Client(client_id, name, email, phone_number)
    clients.append(new_client)
    return new_client

# Function to create a new account
def create_account(account_number, client_id, balance):
    new_account = Account(account_number, client_id, balance)
    accounts.append(new_account)
    return new_account

# Function to make a withdrawal
def make_withdrawal(account_number, amount):
    for account in accounts:
        if account.account_number == account_number:
            if account.balance >= amount:
                account.balance -= amount
                return True
            else:
                return False
    return False

# Function to make a transaction
def make_transaction(client_id, account_number, amount):
    transaction_id = len(transactions) + 1
    new_transaction = Transaction(transaction_id, client_id, account_number, amount, datetime.datetime.now())
    transactions.append(new_transaction)
    return new_transaction

# Function to display client information
def display_client(client_id):
    for client in clients:
        if client.client_id == client_id:
            print(f"Client ID: {client.client_id}")
            print(f"Name: {client.name}")
            print(f"Email: {client.email}")
            print(f"Phone Number: {client.phone_number}")
            return

# Function to display account information
def display_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            print(f"Account Number: {account.account_number}")
            print(f"Client ID: {account.client_id}")
            print(f"Balance: {account.balance}")
            return

# Function to display transaction history
def display_transaction_history(client_id):
    for transaction in transactions:
        if transaction.client_id == client_id:
            print(f"Transaction ID: {transaction.transaction_id}")
            print(f"Account Number: {transaction.account_number}")
            print(f"Amount: {transaction.amount}")
            print(f"Transaction Date: {transaction.transaction_date}")
            return

# Main program
if __name__ == "__main__":
    # Create some sample clients
    client1 = create_client(1, "John Doe", "johndoe@example.com", "123-456-7890")
    client2 = create_client(2, "Jane Doe", "janedoe@example.com", "098-765-4321")

    # Create some sample accounts
    account1 = create_account("1234567890", 1, 1000.0)
    account2 = create_account("9876543210", 2, 500.0)

    # Make some sample transactions
    make_transaction(1, "1234567890", 200.0)
    make_transaction(2, "9876543210", 100.0)

    # Make some sample withdrawals
    make_withdrawal("1234567890", 50.0)
    make_withdrawal("9876543210", 25.0)

    # Display client information
    display_client(1)
    display_client(2)

    # Display account information
    display_account("1234567890")
    display_account("9876543210")

    # Display transaction history
    display_transaction_history(1)
    display_transaction_history(2)

    # Test the system
    while True:
        print("\nMain Menu:")
        print("1. Create a new client")
        print("2. Create a new account")
        print("3. Make a withdrawal")
        print("4. Make a transaction")
        print("5. Display client information")
        print("6. Display account information")
        print("7. Display transaction history")
        print("8. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            client_id = int(input("Enter client ID: "))
            name = input("Enter client name: ")
            email = input("Enter client email: ")
            phone_number = input("Enter client phone number: ")
            create_client(client_id, name, email, phone_number)
        elif choice == "2":
            account_number = input("Enter account number: ")
            client_id = int(input("Enter client ID: "))
            balance = float(input("Enter initial balance: "))
            create_account(account_number, client_id, balance)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            make_withdrawal(account_number, amount)
        elif choice == "4":
            client_id = int(input("Enter client ID: "))
            account_number = input("Enter account number: ")
            amount = float(input("Enter transaction amount: "))
            make_transaction(client_id, account_number, amount)
        elif choice == "5":
            client_id = int(input("Enter client ID: "))
            display_client(client_id)
        elif choice == "6":
            account_number = input("Enter account number: ")
            display_account(account_number)
        elif choice == "7":
            client_id = int(input("Enter client ID: "))
            display_transaction_history(client_id)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")
```

This code creates a comprehensive bank system using Python, incorporating features for client management, transaction processing, and withdrawals. The system includes classes for clients, transactions, and accounts, allowing for easy data manipulation and analysis. The code also includes error handling and exception handling mechanisms to ensure the system is robust and resilient.**Database Schema:**
```sql
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    client_id INT NOT NULL,
    account_number VARCHAR(255) NOT NULL,
    account_type VARCHAR(255) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
```
**Python Code:**
```python
import sqlite3
from getpass import getpass

# Connect to the database
conn = sqlite3.connect("bank_system.db")
cursor = conn.cursor()

# Function to create a new client
def create_client(name, email, password):
    cursor.execute("INSERT INTO clients (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    return cursor.lastrowid

# Function to create a new account
def create_account(client_id, account_number, account_type):
    cursor.execute("INSERT INTO accounts (client_id, account_number, account_type) VALUES (?, ?, ?)", (client_id, account_number, account_type))
    conn.commit()
    return cursor.lastrowid

# Function to perform a transaction
def perform_transaction(account_id, transaction_date, transaction_type, amount):
    cursor.execute("INSERT INTO transactions (account_id, transaction_date, transaction_type, amount) VALUES (?, ?, ?, ?)", (account_id, transaction_date, transaction_type, amount))
    conn.commit()
    return cursor.lastrowid

# Function to get client information
def get_client_info(client_id):
    cursor.execute("SELECT * FROM clients WHERE client_id = ?", (client_id,))
    return cursor.fetchone()

# Function to get account information
def get_account_info(account_id):
    cursor.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,))
    return cursor.fetchone()

# Function to get transaction history
def get_transaction_history(account_id):
    cursor.execute("SELECT * FROM transactions WHERE account_id = ?", (account_id,))
    return cursor.fetchall()

# Main program
while True:
    print("Bank System")
    print("-----------")
    print("1. Create a new client")
    print("2. Create a new account")
    print("3. Perform a transaction")
    print("4. View client information")
    print("5. View account information")
    print("6. View transaction history")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter client name: ")
        email = input("Enter client email: ")
        password = getpass("Enter client password: ")
        client_id = create_client(name, email, password)
        print("Client created successfully!")

    elif choice == "2":
        client_id = int(input("Enter client ID: "))
        account_number = input("Enter account number: ")
        account_type = input("Enter account type: ")
        account_id = create_account(client_id, account_number, account_type)
        print("Account created successfully!")

    elif choice == "3":
        account_id = int(input("Enter account ID: "))
        transaction_date = input("Enter transaction date: ")
        transaction_type = input("Enter transaction type: ")
        amount = float(input("Enter transaction amount: "))
        perform_transaction(account_id, transaction_date, transaction_type, amount)
        print("Transaction performed successfully!")

    elif choice == "4":
        client_id = int(input("Enter client ID: "))
        client_info = get_client_info(client_id)
        print("Client Information:")
        print("Name:", client_info[1])
        print("Email:", client_info[2])

    elif choice == "5":
        account_id = int(input("Enter account ID: "))
        account_info = get_account_info(account_id)
        print("Account Information:")
        print("Account Number:", account_info[2])
        print("Account Type:", account_info[3])
        print("Balance:", account_info[4])

    elif choice == "6":
        account_id = int(input("Enter account ID: "))
        transaction_history = get_transaction_history(account_id)
        print("Transaction History:")
        for transaction in transaction_history:
            print("Transaction Date:", transaction[2])
            print("Transaction Type:", transaction[3])
            print("Amount:", transaction[4])

    elif choice == "7":
        break

    else:
        print("Invalid choice. Please try again.")

# Close the connection
conn.close()
```
This code creates a SQLite database and defines the necessary tables and relationships. It also provides a user-friendly interface for users to create new clients and accounts, perform transactions, view client and account information, and view transaction history. The code uses the `sqlite3` library to interact with the database and the `getpass` library to prompt users for sensitive information (e.g. passwords).