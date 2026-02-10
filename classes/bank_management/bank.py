################################################################################
from time import time
from account import Account
from helpers import generate_id
################################################################################
class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.accounts = {}

    def open_account(self, owner, amount=500):
        new_account = Account(owner, amount)
        self.accounts[new_account.account_number] = new_account
        new_account.add_transaction("Account Created", amount)
        return new_account.account_number

    def transfer(self, sender_number, receiver_number, amount):
        if sender_number in self and receiver_number in self:
            sender = self.accounts[sender_number]
            receiver = self.accounts[receiver_number]
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                sender.add_transaction(f"Transfer To {receiver.owner.full_name}", amount)
                receiver.add_transaction(f"Transfer From {sender.owner.full_name}", amount)
                return True
            else:
                print(f"Sender {sender.owner.full_name} don't have enough funds")
                return False
        else:
            print("Sender or Receiver Account not found")
            return False

    def close_account(self, account_number):
        if account_number in self:
            existed_account = self.accounts[account_number]
            if existed_account.is_empty():
                existed_account.status = "CLOSED"
                existed_account.add_transaction("Account Closed", 0)
                return True
            else:
                print(f"account number ({account_number}) is not empty to be closed")
        else:
            print(f"account number ({account_number}) is not found to be closed")
        return False

    def disable_account(self, account_number):
        if account_number in self:
            existed_account = self.accounts[account_number]
            existed_account.status = "DISABLED"
            existed_account.add_transaction("Account Disabled", 0)
            return True
        print(f"account number ({account_number}) is not found to be disabled")
        return False

    def __len__(self):
        return len(self.accounts)

    def __iter__(self):
        return iter(self.accounts)
    def __next__(self):
        return next(self.accounts)
    def __reversed__(self):
        return reversed(self.accounts)

    def __getitem__(self, account_number):
        return self.accounts[account_number]

    def __contains__(self, account_number):
        return account_number in self.accounts

    def __str__(self):
        return f"{self.name} Bank is located in {self.location} and has {len(self)} accounts"
    def __repr__(self):
        return self.__str__()
