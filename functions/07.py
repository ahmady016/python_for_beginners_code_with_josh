# build a function to display user's info using a variable number of keyword arguments **:
# the function a variable number of keyword arguments
# the function print the given user's info
########################################################
print("##################################")
print("user info program")
print("##################################")
########################################################
def display_user_info(**user_info):
    print("User Info:")
    print("----------")
    for key, value in user_info.items():
        print(f"{key}: {value}")
########################################################
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_country = input("Enter your country: ")
user_email = input("Enter your email: ")
user_password = input("Enter your password: ")
print("--------------------------------")

display_user_info(name=user_name, age=user_age, country=user_country, email=user_email, password=user_password)
########################################################
