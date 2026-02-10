# build a simple bank accounts management that:
# ------------------------------------------------------------------------------
# allow customers to create an account
# allow customers to deposit money into their account
# allow customers to withdraw money from their account
# allow customers to transfer money to another account
# allow customers to granted a loan
# allow customers to pay back a loan
# allow customers to check their account balance
# allow customers to view their transaction history
# allow customers to close their account
# note: loan granted if they have at least 10% of loan amount in balance
# note: account only close account if the balance is $0 and there is no outstanding loan
#################################################################################
# test the bank accounts management:
# -------------------------------------------------------------------------------
# create 3 customers
# create 6 accounts 2 for each customer
# create a 2 banks
# add 3 accounts to each bank but one account for each customer
#################################################################################
# then test the bank accounts management
# -------------------------------------------------------------------------------
# in the first bank:
# deposit money into the first account
# withdraw money from the first account
# transfer money from the first account to the second account
# grant a loan to the first account
# pay back a loan from the first account
# check the balance of the first account
# view the transaction history of the first account
# close the first account
# in the second bank:
# deposit money into the first account
# withdraw money from the first account
# transfer money from the first account to the second account
# grant a loan to the first account
# pay back a loan from the first account
# check the balance of the first account
# view the transaction history of the first account
# close the first account
#################################################################################
from customer import Customer
from bank import Bank
#################################################################################
ahmed = Customer("Ahmed", "Hamdy", "123 Main St", "01143680055", 1997, "Male")
sayed = Customer("Sayed",  "Gaber", "456 Main St", "01143680055", 1992, "Male")
eman = Customer("Eman", "Nasr", "123 Main St", "01143680055", 1987, "Female")
################################################################################
cib_bank = Bank("CIB Bank", "cairo")
qnb_bank = Bank("QNB Bank", "fayoum")
################################################################################
ahmed_account_01_number = cib_bank.open_account(ahmed, 1500)
ahmed_account_02_number = qnb_bank.open_account(ahmed, 2500)

sayed_account_01_number = cib_bank.open_account(sayed, 3600)
sayed_account_02_number = qnb_bank.open_account(sayed, 7500)

eman_account_01_number = cib_bank.open_account(eman, 4500)
eman_account_02_number = qnb_bank.open_account(eman, 8750)
################################################################################
print("######################################")
print("Simple Bank Management Program Started")
print("######################################")
################################################################################
# cib bank transactions
################################################################################
ahmed_account_01 = cib_bank[ahmed_account_01_number]
sayed_account_01 = cib_bank[sayed_account_01_number]

print("--------------------------------")
print("ahmed account 01 balance:", ahmed_account_01.get_balance())
print("--------------------------------")

print(f"withdraw 800 from ahmed account 01: {ahmed_account_01.withdraw(800)}")
print(f"deposit 2000 to ahmed account 01: {ahmed_account_01.deposit(2000)}")
print(f"withdraw 1200 from ahmed account 01: {ahmed_account_01.withdraw(1200)}")

print(f"Transfer 1000 from ahmed account 01 to sayed account 01: {cib_bank.transfer(ahmed_account_01_number, sayed_account_01_number, 1000)}")
print("--------------------------------")

print("ahmed account 01 balance:", ahmed_account_01.get_balance())
print("--------------------------------")

print("Give loan 2500 to ahmed account 01:")
print(f"{ahmed_account_01.get_loan(2500)}")
print("Pay loan 500 from ahmed account 01:")
print(f"{ahmed_account_01.pay_loan(500)}")
print("Pay loan 1000 from ahmed account 01:")
print(f"{ahmed_account_01.pay_loan(1000)}")
print("Pay loan 500 from ahmed account 01:")
print(f"{ahmed_account_01.pay_loan(500)}")

print("--------------------------------")
print("ahmed account 01 balance:", ahmed_account_01.get_balance())
print("--------------------------------")
print(f"ahmed account 01 transactions ({ahmed_account_01.get_transactions_count()}):")
print(f"{ahmed_account_01.get_formatted_transactions()}")
print("--------------------------------")

print(f"close ahmed account 01: {cib_bank.close_account(ahmed_account_01_number)}")
print("--------------------------------")

print(f"Pay loan 500 from ahmed account 01: {ahmed_account_01.pay_loan(500)}")
print(f"withdraw 500 from ahmed account 01: {ahmed_account_01.withdraw(500)}")

print("--------------------------------")
print(f"close ahmed account 01: {cib_bank.close_account(ahmed_account_01_number)}")

print("--------------------------------")
print("ahmed account 01 balance:", ahmed_account_01.get_balance())
print(f"ahmed account 01 transactions ({ahmed_account_01.get_transactions_count()}):")
print(f"{ahmed_account_01.get_formatted_transactions()}")
################################################################################
# qnb bank transactions
################################################################################
ahmed_account_02 = qnb_bank[ahmed_account_02_number]
sayed_account_02 = qnb_bank[sayed_account_02_number]

print("--------------------------------")
print("ahmed account 02 balance:", ahmed_account_02.get_balance())
print("--------------------------------")

print(f"withdraw 800 from ahmed account 02: {ahmed_account_02.withdraw(800)}")
print(f"deposit 2000 to ahmed account 02: {ahmed_account_02.deposit(1500)}")
print(f"withdraw 1200 from ahmed account 02: {ahmed_account_02.withdraw(1200)}")

print(f"Transfer 1000 from ahmed account 02 to sayed account 02: {qnb_bank.transfer(ahmed_account_02_number, sayed_account_02_number, 1000)}")
print("--------------------------------")

print("ahmed account 02 balance:", ahmed_account_02.get_balance())
print("--------------------------------")

print("Give loan 5000 to ahmed account 02:")
print(f"{ahmed_account_02.get_loan(5000)}")
print("Pay loan 1500 from ahmed account 02:")
print(f"{ahmed_account_02.pay_loan(1500)}")
print("Pay loan 1000 from ahmed account 02:")
print(f"{ahmed_account_02.pay_loan(1000)}")
print("Pay loan 500 from ahmed account 02:")
print(f"{ahmed_account_02.pay_loan(500)}")

print("--------------------------------")
print("ahmed account 02 balance:", ahmed_account_02.get_balance())
print(f"ahmed account 02 transactions ({ahmed_account_02.get_transactions_count()}):")
print(f"{ahmed_account_02.get_formatted_transactions()}")
print("--------------------------------")

print(f"close ahmed account 02: {qnb_bank.close_account(ahmed_account_02_number)}")

print(f"Pay loan 2000 from ahmed account 02: {ahmed_account_02.pay_loan(2000)}")
print(f"withdraw 1000 from ahmed account 02: {ahmed_account_02.withdraw(1000)}")

print("--------------------------------")
print(f"close ahmed account 02: {qnb_bank.close_account(ahmed_account_02_number)}")

print("--------------------------------")
print("ahmed account 02 balance:", ahmed_account_02.get_balance())
print(f"ahmed account 02 transactions ({ahmed_account_02.get_transactions_count()}):")
print(f"{ahmed_account_02.get_formatted_transactions()}")
print("--------------------------------")
################################################################################
# qnb bank transactions
################################################################################
print("######################################")
print("Simple Bank Management Program Finished")
print("######################################")
################################################################################
