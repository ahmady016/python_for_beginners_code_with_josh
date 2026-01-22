# create an expense tracker:
# collect the user's name and income
# collect the user's foods expense amount
# collect the user's apartment rent expense amount
# collect the user's other expense amount
# display the user's total expense like: Ahmed's total expense: $500
# estimate the remaining amount like: Ahmed has $300 remaining

user_name = input("Enter your name: ").upper()
income = int(input("Enter your income: "))

foods_expense = int(input("Enter your foods expense: "))
apartment_rent_expense = int(input("Enter your apartment rent expense: "))
other_expense = int(input("Enter your other expense: "))

total_expense = foods_expense + apartment_rent_expense + other_expense
remaining_amount = income - total_expense

print("------------------------------")
print(f"{user_name}'s total expense: ${total_expense}")
print(f"{user_name} has ${remaining_amount} remaining")
print("------------------------------")
