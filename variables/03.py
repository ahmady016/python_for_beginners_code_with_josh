# estimate the price cost for family gusts in a resort hotel:
# given the room price of $750 per night
# and the number of nights is 7
# and the resort offers a 20% discount

room_price = 600
number_of_nights = 7
discount = 0.2

total_cost = room_price * number_of_nights
total_cost_after_discount = total_cost * (1 - discount)

print("-----------------------------------------")
print("cost for family guests in a resort hotel")
print("-----------------------------------------")
print("total cost:", total_cost)
print("total cost after discount:", total_cost_after_discount)
print("-----------------------------------------")
