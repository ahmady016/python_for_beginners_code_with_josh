# estimate the total price for 3 product items:
# collect the user's name
# collect each 3 product price
# check if the product01 price is the most expensive then give him 66% discount
# check if the product02 price is the most expensive then give him 50% discount
# check if the product03 price is the most expensive then give him 33% discount
# print the total const before and after discount

print("total price calculator")
print("-------------------------")
user_name = input("Enter your name: ").upper()
product01 = float(input("Enter the price of product#1: "))
product02 = float(input("Enter the price of product#2: "))
product03 = float(input("Enter the price of product#3: "))
print("-------------------------")

total_cost = product01 + product02 + product03
total_cost_after_discount = total_cost

if product01 > product02 and product01 > product03:
    print(f"product#1 is the most expensive and you will get 66% discount")
    total_cost_after_discount *= 0.33
elif product02 > product01 and product02 > product03:
    print(f"product#2 is the most expensive and you will get 50% discount")
    total_cost_after_discount *= 0.5
elif product03 > product01 and product03 > product02:
    print(f"product#3 is the most expensive and you will get 33% discount")
    total_cost_after_discount *= 0.66
else:
    print("all 3 products have the same price and there is no discount")

print("total cost:", total_cost)
print("total cost after discount:", total_cost_after_discount)
print("-------------------------")
