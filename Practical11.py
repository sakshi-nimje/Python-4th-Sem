'''Using Object oriented Programming, write a program for opening a Bank account,deposit of money and withdrawal of money. Also generate a 4 digit unique code for each transaction.
'''

import random

class Bank_Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        code = random.randint(1000, 9999)
        self.transactions.append(('deposit', amount, code))
        print(f"\nDeposited {amount} into account of {self.name}. Transaction code: {code}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient amount!!!.")
        else:
            self.balance -= amount
            code = random.randint(1000, 9999)
            self.transactions.append(('withdraw', amount, code))
            print(f"\nWithdrew {amount} from account of {self.name}. Transaction code: {code}")

    def get_balance(self):
        print(f"\nBalance of account {self.name}: {self.balance}")

    def get_transactions(self):
        for t in self.transactions:
            print(f"\nTransaction type: {t[0]}, amount: {t[1]}, code: {t[2]}")

account = Bank_Account("STEVE")
account.deposit(10000)
account.withdraw(5000)
account.get_balance()
account.get_transactions()

'''
Output:
Deposited 10000 into account of STEVE. Transaction code: 7593

Withdrew 5000 from account of STEVE. Transaction code: 1810

Balance of account STEVE: 5000

Transaction type: deposit, amount: 10000, code: 7593

'''
