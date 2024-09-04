from datetime import datetime
import pandas as pd
class Bank_Transaction:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id, owner):
        if account_id not in self.accounts:
            self.accounts[account_id] = {
                'owner': owner,
                'balance': 0.0,
                'transactions': []
            }
            print(f"Account created for {owner} with ID {account_id}.")
        else:
            print("Account already exists.")

    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id]['balance'] += amount
            owner = self.accounts[account_id]['owner']
            transaction_details = f"Deposited: ${amount:.2f} by {owner} at {datetime.now()}"
            self.accounts[account_id]['transactions'].append(transaction_details)
            print(f"Deposited ${amount:.2f} to account {account_id} belonging to {owner}.")
        else:
            print("Account does not exist.")

    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            if self.accounts[account_id]['balance'] >= amount:
                self.accounts[account_id]['balance'] -= amount
                owner = self.accounts[account_id]['owner']
                transaction_details = f"Withdrew: ${amount:.2f} by {owner} at {datetime.now()}"
                self.accounts[account_id]['transactions'].append(transaction_details)
                print(f"Withdrew ${amount:.2f} from account {account_id} belonging to {owner}.")
            else:
                print("Insufficient balance.")
        else:
            print("Account does not exist.")

    def get_balance(self, account_id):
        if account_id in self.accounts:
            owner = self.accounts[account_id]['owner']
            balance = self.accounts[account_id]['balance']
            return owner, balance
        else:
            print("Account does not exist.")
            return None, None

    def get_transactions(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]['transactions']
        else:
            print("Account does not exist.")
            return None

bank = Bank_Transaction()
while True:
    print("\nBANK_MODEL")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1': 
        account_id = input("Account ID: ")
        owner = input("Owner Name: ")
        bank.create_account(account_id, owner)
    elif choice == '2': 
        account_id = input("Account ID: ")
        amount = float(input("Enter amount: "))
        bank.deposit(account_id, amount)
    elif choice == '3':  
        account_id = input("Account ID: ")
        amount = float(input("Enter amount: "))
        bank.withdraw(account_id, amount)
    elif choice == '4':
        account_id = input("Account ID: ")
        owner, balance = bank.get_balance(account_id)
        if balance is not None:
            print(f"Balance of account ID {account_id} belonging to/ {owner}: ${balance:.2f}")
    elif choice == '5': 
        account_id = input("Account ID: ")
        transactions = bank.get_transactions(account_id)
        if transactions is not None:
            print(f"Transactions for account ID {account_id}:")
            for transaction in transactions:
                print(transaction)
    elif choice == '6': 
        print("Exiting...","\n after exiting all the values are erased")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 6.")
