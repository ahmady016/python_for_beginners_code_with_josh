# estimate the total shipping packages by weight for 3 packages:
# input the wight of each package
# offer a 20% discount on the shipping weight
# print total cost for shipping the packages like: Total Shipping: 500kg

weight1 = float(input("Enter the weight of package #1: "))
weight2 = float(input("Enter the weight of package #2: "))
weight3 = float(input("Enter the weight of package #3: "))

discount = 0.2
total_weight = weight1 + weight2 + weight3
total_weight_after_discount = total_weight * (1 - discount)

print("------------------------------")
print(f"Total Shipping: {total_weight}kg")
print(f"Total Shipping After 20% Discount: {total_weight_after_discount}kg")
print("------------------------------")
