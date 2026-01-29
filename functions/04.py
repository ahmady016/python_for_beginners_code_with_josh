# build a BMI calculator program using two functions:
# the first one calculate and return the BMI based on weight and height
# as (BMI = weight / height^2)
# the second one takes the BMI and tell the user if they are (underweight, normal, overweight)
# in the main program ask for the number of people
# and collect the user's name, weight and height for each one
# and print if the user is (underweight, normal, overweight)

def calculate_bmi(weight, height):
    return weight / height ** 2

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 25:
        return "Normal"
    else:
        return "Overweight"

print("BMI Calculator Program")
print("-------------------------")
number_of_people = int(input("Enter the number of people: "))
print("-------------------------")

for i in range(number_of_people):
    user_name = input("Enter your name: ").upper()
    user_weight = float(input("Enter your weight in kg: "))
    user_height = float(input("Enter your height in cm: "))
    print("-------------------------")

    bmi = calculate_bmi(user_weight, user_height / 100)
    category = get_bmi_category(bmi)
    print(f"Hi {user_name}, your BMI is {bmi:.2f} and you are {category} person")
    print("-------------------------")

print("Program Finished")
print("-------------------------")
