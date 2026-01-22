# create a discount status calculator by a specific discount code:
# collect the user's name
# collect the discount code
# if the discount code is qwerty3690 offer a 30% discount
# otherwise print not a valid discount code and there is no discount
# display the discounted status like: Ahmed has a discount of 30%
# or not a valid discount code and there is no discount

print("discount status calculator")
print("-------------------------")
user_name = input("Enter your name: ").upper()
discount_code = input("Enter the discount code: ").lower()
print("-------------------------")

print("discount status")
print("-------------------------")

if discount_code == "qwerty3690":
    print(f"{user_name} has a discount of 30%")
else:
    print("not a valid discount code and there is no discount")

print("-------------------------")
