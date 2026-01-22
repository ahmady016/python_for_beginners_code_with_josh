# create a flight cost estimator for a passenger:
# collect the user's name and distinction
# collect the bags wight in kg and the flight class [Business, Economy]
# check if the bags weight is more than 20kg then the price is $125 otherwise $50
# and check the flight class if it is Business then the price is $750 otherwise $350
# estimate the total cost for the flight
# display the total cost for the flight like: Ahmed has a flight to New York and has a total cost of $900

print("flight cost estimator")
print("-------------------------")
user_name = input("Enter your name: ").upper()
distinction = input("Enter your distinction: ").upper()
bags_weight = float(input("Enter the bags weight in kg: "))
flight_class = input("Enter the flight class [Business, Economy]: ").lower()

bags_cost = 50
if bags_weight > 20:
    bags_cost = 125

flight_cost = 350
if flight_class == "business":
    flight_cost = 750

ticket_cost = bags_cost + flight_cost
print("-------------------------")
print(f"{user_name} has a flight to {distinction} and has a ticket price of ${ticket_cost:.2f}")
print("-------------------------")
