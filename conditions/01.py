# create a discount for a trip:
# collect the user's name
# collect the trip destination
# collect the trip type [bus, train, flight]
# collect the expected trip cost
# if the trip type is flight and the cost is more than $700 offer a 40% discount
# display the discounted trip status like: Ahmed has a flight to New York and has a discount of 40%
# display the non-discounted trip status like: Ahmed has a flight to New York and has no discount

print("trip discount calculator")
print("-------------------------")
user_name = input("Enter your name: ").upper()
trip_destination = input("Enter the trip destination: ").upper()
trip_type = input("Enter the trip type [bus, train, flight]: ").lower()
trip_cost = float(input("Enter the expected trip cost: "))
print("-------------------------")

print("trip discount status")
print("-------------------------")

if trip_type == "flight" and trip_cost > 700:
    print(f"{user_name} has a trip to {trip_destination} by flight and has a discount 40% off")
else:
    print(f"{user_name} has a trip to {trip_destination} by {trip_type} and has no discount")

print("-------------------------")
