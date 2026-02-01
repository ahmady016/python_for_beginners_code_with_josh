# build a income monthly average calculator program:
# collect the user's name, income and number of months
# calculate and print the user's income monthly average
########################################################
def calculate_monthly_average(income, months):
    return round(float(income) / int(months), 2)
########################################################
print("#########################################")
print("income monthly average calculator program")
print("#########################################")
########################################################
user_name = input("Enter your name: ").upper()
income = input("Enter your income: ")
months = input("Enter the number of months: ")
print("-----------------------------------------")
########################################################
try:
    monthly_average = calculate_monthly_average(income, months)
    print(f"Hi {user_name}, your monthly average is ${monthly_average}")
except ZeroDivisionError as error:
    print("you can't divide by zero")
    print(error)
except ValueError as error:
    print("you must enter a valid numbers")
    print(error)
except TypeError as error:
    print("you must enter a valid numbers")
    print(error)
except Exception as error:
    print("something went wrong")
    print(error)
finally:
    print(f"Thank you {user_name} for using our program")
########################################################
print("#########################################")
print("income monthly average calculator program completed successfully")
print("#########################################")
########################################################
