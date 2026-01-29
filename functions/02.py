# create a function that add on extra flight charges
# the function takes a base fare then ask you if you have baggage
# if yes then add 35 to the base fare
# before returning the total fare you need to add 20% tax
# print the total cost after extras and tax

def calculate_flight_cost(base_fare):
    if input("Do you have baggage? [yes/no]: ").lower() == "yes":
        base_fare += 35
    return base_fare * 1.2

print("flight cost calculator")
print("----------------------")
user_name = input("Enter your name: ").upper()
flight_base_fare = float(input("Enter your flight base fare: "))

total_cost = calculate_flight_cost(200)
print(f"Your Flight Total Cost is: ${total_cost:.2f}")
