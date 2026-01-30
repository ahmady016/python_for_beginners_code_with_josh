# build a BMI calculator program using helpers module as
# first ask for the number of people
# and collect the user's name, weight and height for each one
# then call the bmi_calculator function and print the result

from helpers import bmi_calculator

print("BMI Calculator Program")
print("-------------------------")
number_of_people = int(input("Enter the number of people: "))
print("-------------------------")

for i in range(number_of_people):
    user_name = input("Enter your name: ").upper()
    user_weight = float(input("Enter your weight in kg: "))
    user_height = float(input("Enter your height in cm: "))
    print("-------------------------")
    print(bmi_calculator(user_name, user_weight, user_height / 100))
    print("-------------------------")

print("BMI Calculator Program Completed Successfully")
print("-----------------------------")
