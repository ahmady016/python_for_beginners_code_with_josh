# build a program to display variable types in python:
# input the user's name => string
# input the user's phone number => string
# input the user's age => integer
# input the user's weight => float
# input the user's job status => boolean
# and convert each one of them to the correct type
##########################################################
print("##################################")
print("Program to display data types in python")
print("##################################")
##########################################################
user_name = input("Enter your name: ")
user_phone_number = input("Enter your phone number: ")
user_age = input("Enter your age: ")
user_weight = input("Enter your weight: ")
user_job_status = input("Enter your job status: [True/False] ")
##########################################################
user_age = int(user_age)
user_weight = float(user_weight)
user_job_status = bool(user_job_status)
##########################################################
print("##################################")
print(f"Name Type: {type(user_name)}")
print(f"Phone Number Type: {type(user_phone_number)}")
print(f"Phone Number isDigit: {user_phone_number.isdigit()}")
print(f"Age Type: {type(user_age)}")
print(f"Weight Type: {type(user_weight)}")
print(f"Job Status Type: {type(user_job_status)}")
##########################################################
print("##################################")
print("Program Finished")
print("##################################")
##########################################################
