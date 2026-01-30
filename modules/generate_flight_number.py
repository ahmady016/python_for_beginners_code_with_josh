# build a flight booking program using the random module as:
# ask the user to enter passenger name or 0 to quit
# loop till the user enter 0 and generate a random flight number
# and print the passenger name and flight number

from random import randint

print("flight booking program")
print("-------------------------")
user_name = input("Enter your name or 0 to quit: ").upper()
print("-------------------------")

while user_name != "0":
    flight_number = randint(1001, 9999)
    print(f"Hi {user_name} your flight number is {flight_number}")
    print("-------------------------")
    user_name = input("Enter your name or 0 to quit: ").upper()
    print("-------------------------")

if user_name == "0":
    print("You have quit the program")

print("Flight Booking Program Completed Successfully")
print("-------------------------")
