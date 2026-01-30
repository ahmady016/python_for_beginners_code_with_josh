# rebuild the adventure planning program:
# use the functions from the helpers module
# that ask the user to enter 1 to start and loops tell the user enter 0 to quit
# in each loop help the user to choose a destination asking for the kind of trip [beach, city, mountains]
# for each answer call the matching function from the helpers module

from helpers import beach_trip, city_trip, mountains_trip

print("adventure planning program")
print("--------------------------")
user_name = input("Enter your name: ").upper()
start = int(input("Enter 1 to start and 0 to quit: "))
print("--------------------------------------")

while start == 1:
    print("let's choose your destination:")
    print("------------------------------")
    trip_type = input("Enter the trip type [beach, city, mountains]: ").lower()
    print("--------------------------------------")
    if trip_type == "beach":
        beach_trip()
    elif trip_type == "city":
        city_trip()
    elif trip_type == "mountains":
        mountains_trip()
    else:
        print("That trip type is not available")

    start = int(input("Enter 1 to start and 0 to quit: "))

print(f"have fun on your trip {user_name}")
print("--------------------------")
