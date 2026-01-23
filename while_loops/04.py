# build a ticket booking program:
# collect the user's name
# ask the user if he want to book a ticket [y/n]
# if the user responds "y" print "ticket#01 has been booked"
# loop until the user responds "n"

print("ticket booking program")
print("-------------------------")
user_name = input("Enter your name: ").upper()
user_response = input("Do you want to book a ticket? [y/n]: ").lower()
print("-------------------------")

ticket_count = 0
while user_response == "y":
    ticket_count += 1
    print(f"Ok {user_name}, ticket#{ticket_count} has been booked")
    print("-------------------------")
    user_response = input("Do you want to book a ticket? [y/n]: ").lower()
    print("-------------------------")

print(f"Thanks for booking {user_name} you have booked {ticket_count} tickets")
print("-------------------------")
