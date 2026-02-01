# build a function to calculate the total price of a set of shopping items using packing and unpacking
# the function takes comma separated prices
# the function returns the total price of the items

def calculate_total_cost(*prices):
    total_cost = 0
    for price in prices:
        total_cost += float(price)
    return total_cost

total_cost = calculate_total_cost(180, 70, 60, 120, 245)
print(f"Total of (180, 70, 60, 120, 245) is: {total_cost:.2f}")
