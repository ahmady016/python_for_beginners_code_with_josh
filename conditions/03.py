# create trip type recommendation program by user trip balance:
# collect the user's name and trip balance
# if the trip balance is more than $1000 recommend a (Flight-To-The-Beach) trip
# if the trip balance is between $400 and $1000 recommend a (road) trip
# if the trip balance is less than $400 recommend a (stay-cation) trip
# display the trip recommendation like: Ahmed has a (Flight-To-The-Beach) trip recommendation
# print have fun on your trip at the end of the program

print("trip recommendation program")
print("-------------------------")
user_name = input("Enter your name: ").upper()
trip_balance = float(input("Enter your trip balance: "))
print("-------------------------")

print("trip recommendation")
print("-------------------------")

if trip_balance > 1000:
    print(f"{user_name} has a (Flight-To-The-Beach) trip recommendation")
elif trip_balance >= 400 and trip_balance <= 1000:
    print(f"{user_name} has a (road) trip recommendation")
else:
    print(f"{user_name} has a (stay-cation) trip recommendation")

print("have fun on your trip")
print("-------------------------")
