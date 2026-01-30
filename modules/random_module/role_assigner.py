# build a role assigner program using the random module as:
# generate a random number between 1 and 3
# if the number is 1 assign the user to role of "admin"
# if the number is 2 assign the user to role of "supervisor"
# if the number is 3 assign the user to role of "guest"
# at the end print each role assignees count

from random import randint

print("role assigner program")
print("---------------------")

admin_count = 0
supervisor_count = 0
guest_count = 0

user_response = input("would you like to randomly assigned to a role [admin, supervisor, guest]? [y/n]: ").lower()
print("---------------------")

users_count = 0
while user_response == "y":
    users_count += 1
    role = randint(1, 3)
    if role == 1:
        admin_count += 1
        print(f"user#{users_count} has been assigned to admin role")
    elif role == 2:
        supervisor_count += 1
        print(f"user#{users_count} has been assigned to supervisor role")
    else:
        guest_count += 1
        print(f"user#{users_count} has been assigned to guest role")

    user_response = input("would you like to randomly assigned to a role [admin, supervisor, guest]? [y/n]: ").lower()
    print("---------------------")

print("---------------------")
print("users count:", users_count)
print(f"admin count: {admin_count}")
print(f"supervisor count: {supervisor_count}")
print(f"guest count: {guest_count}")

print("Role Assigner Program Completed Successfully")
print("-------------------------")
