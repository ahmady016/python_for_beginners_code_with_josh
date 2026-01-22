# estimate the total cost for a car rent:
# input the number of days for renting
# input the car rent price per day
# print total cost for renting the car like: Total Car Rent: $500

car_rent_price = int(input("Enter the car rent price per day: "))
number_of_days = int(input("Enter the number of days for renting: "))
total_cost = car_rent_price * number_of_days

print("------------------------------")
print(f"Total Car Rent: ${total_cost:.2f}")
print("------------------------------")
