# create a bank balance function that accept a balance
# and check the balance if it is $1000 or more return True otherwise return False
# and build a program that ask for the number of bank customers
# and depending on the number of customers loop and collect the customer's name and balance
# and print if each one have enough balance or not

def has_enough_fund(balance):
    return True if balance >= 1000 else False

print("bank balance checker program")
print("----------------------------")

number_of_customers = int(input("Enter the number of customers: "))
print("----------------------------")

for i in range(number_of_customers):
    customer_name = input(f"Enter customer #{i + 1} name: ").upper()
    customer_balance = float(input(f"Enter customer #{i + 1} current balance: "))
    print("----------------------------")
    if has_enough_fund(customer_balance):
        print(f"{customer_name} has enough funds")
    else:
        print(f"{customer_name} does not have enough funds")

print("----------------------------")
