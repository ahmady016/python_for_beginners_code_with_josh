# build a hotel recommendation program:
# collect the user's name
# ask the user if he want a hotel or resort
# if the user wants a resort ask him his current budget
# if the budget is more than $1000 recommend a (Six Senses) resort
# otherwise recommend a (Four Season) resort
# and if the user want a hotel recommend the nearest (Hilton) hotel

print("hotel recommendation program")
print("--------------------------------------")
user_name = input("Enter your name: ").upper()
user_accommodation = input("Do you want a (hotel or resort)?: ").lower()

if user_accommodation == "resort":
    budget = float(input("Enter your budget: "))
    print("--------------------------------------")
    if budget > 1000:
        print(f"{user_name} go to (Six Senses) resort")
    else:
        print(f"{user_name} go to (Four Season) resort")
else:
    print("--------------------------------------")
    print(f"{user_name} go to the nearest (Hilton) hotel")

print("--------------------------------------")
