# build a shopping list calculator program as:
# collect the user name and create an empty dictionary
# and ask the user to enter a shopping item and its price separated by comma
# loop until the user enter 0 to quit
# at the end print the total cost of the shopping list
#################################################
print("####################")
print("shopping list calculator program")
print("####################")
#################################################
user_name = input("Enter your name: ").upper()
print("----------------------------------------")
#################################################
shopping_list = {}
user_response = input("Enter a shopping item and its price separated by comma: ")
while user_response != "0":
    (item, price) = user_response.split(", ")
    if item in shopping_list:
        print(f"Sorry {item} is already in the list")
        continue
    shopping_list[item] = price
    user_response = input("Enter a shopping item and its price separated by comma: ")
#################################################
print("----------------------------------------")
total_cost = 0
for item in shopping_list:
    total_cost += float(shopping_list.get(item))
print(f"The Total Cost of Shopping List: ${total_cost:.2f}")
#################################################
print("###############################################")
print(f"Thanks {user_name} for using our shopping list calculator program")
print("###############################################")
#################################################
