#########################################################################################
from datetime import datetime
from helpers import generate_id
#########################################################################################
class Account:
    def __init__(self, owner ,balance=500):
        self.account_number = f"{datetime.timestamp(datetime.now())}-{generate_id(6)}"
        self.owner = owner
        self.balance = balance
        self.loan = 0
        self.status = "OPENED"
        self.transactions = {}

    def add_transaction(self, type, amount):
        self.transactions[generate_id(12)] = {
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "type": type,
            "amount": amount,
            "balance_after": self.balance
        }

    def get_formatted_transactions(self):
        if not self.transactions:
            return "This account has No transactions right now"
        return "\n".join([f"{transaction['type']} at {transaction['time']} with {transaction['amount']} amount and balance {transaction['balance_after']}" for transaction in self.transactions.values()])

    def get_transactions(self):
        if not self.transactions:
            print("This account has No transactions right now")
            return []
        return self.transactions.values()

    def get_transactions_count(self):
        if not self.transactions:
            print("This account has No transactions right now")
            return 0
        return len(self.transactions)

    def get_deposits_transactions(self):
        if self.status not in ["CLOSED", "DISABLED"]:
            return [transaction for transaction in self.transactions.values() if transaction["type"] == "Deposit"]
        print("This account is closed or disabled")
        return []
    def get_withdrawals_transactions(self):
        if self.status not in ["CLOSED", "DISABLED"]:
            return [transaction for transaction in self.transactions.values() if transaction["type"] == "Withdraw"]
        print("This account is closed or disabled")
        return []
    def get_loans_transactions(self):
        if self.status not in ["CLOSED", "DISABLED"]:
            return [transaction for transaction in self.transactions.values() if transaction["type"] == "get_Loan"]
        print("This account is closed or disabled")
        return []
    def get_payments_transactions(self):
        if self.status not in ["CLOSED", "DISABLED"]:
            return [transaction for transaction in self.transactions.values() if transaction["type"] == "pay_Loan"]
        print("This account is closed or disabled")
        return []

    def get_balance(self):
        return self.balance

    def is_empty(self):
        return self.balance == 0 and self.loan == 0

    def is_loaned(self):
        return self.loan > 0

    def deposit(self, amount):
        if self.status in ["CLOSED", "DISABLED"]:
            print("This account is closed or disabled")
        elif amount <= 0:
            print("Please enter a valid amount")
        else:
            self.balance += amount
            self.add_transaction("Deposit", amount)
        return self.balance
    def withdraw(self, amount):
        if self.status in ["CLOSED", "DISABLED"]:
            print("This account is closed or disabled")
        elif amount <= 0:
            print("Please enter a valid amount")
        elif amount > self.balance:
            print("You don't have enough funds")
        else:
            self.balance -= amount
            self.add_transaction("Withdraw", amount)
        return self.balance

    def get_loan(self, amount):
        if self.status in ["CLOSED", "DISABLED"]:
            print("This account is closed or disabled")
        elif amount <= 0:
            print("Please enter a valid amount")
        elif self.balance < (amount * 0.1):
            print("You don't have enough funds")
        else:
            self.balance += amount
            self.loan += amount
            self.add_transaction("Grant Loan", amount)
        return self.balance
    def pay_loan(self, amount):
        if self.status in ["CLOSED", "DISABLED"]:
            print("This account is closed or disabled")
        elif self.loan == 0:
            print("You don't have any loan")
        elif amount <= 0:
            print("Please enter a valid amount")
        else:
            amount = min(amount, self.loan)
            self.balance -= amount
            self.loan -= amount
            self.add_transaction("Pay Loan", amount)
        return self.balance

    def __len__(self):
        return len(self.transactions)

    def __str__(self):
        return f"""-------------------------
    Account Number: {self.account_number}
    Owner: {self.owner.full_name}
    Balance: {self.balance}
    Loan: {self.loan}
    Transactions: {len(self)}
--------------------------"""

    def __repr__(self):
        return self.__str__()
