# create a user_id and display it to the user:
# by collecting the user's name, age and mobile number
# and display the user_id like: Ahmed_45_01143680055

user_name = input("Enter your name: ").upper()
user_age = input("Enter your age: ")
user_mobile_number = input("Enter your mobile number: ")

user_id = f"{user_name}_{user_age}_{user_mobile_number}"
print("------------------------------")
print(f"Your User ID: {user_id}")
print("------------------------------")
