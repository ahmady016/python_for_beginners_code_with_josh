# build a Admin login program:
# collect the username and password from the user
# the user has only 3 attempts
# check if the username is "admin" and the password is "2026"
# then print "welcome admin"
# otherwise print "incorrect username or password try again"
# if the user enters the wrong username or password 3 times print "Opps you reached 3 attempts and you are not the admin"

print("Admin login program")
print("-------------------")

MAX_ATTEMPTS = 3
for attempt in range(MAX_ATTEMPTS):
    print(f"attempt#{attempt + 1} of {MAX_ATTEMPTS}")
    print("-------------------------")
    user_name = input("Enter your name: ").lower()
    password = input("Enter your password: ")
    print("-------------------------")
    if user_name == "admin" and password == "2026":
        print("welcome admin")
        break
    elif attempt < MAX_ATTEMPTS - 1:
        print("incorrect username or password try again")
        print("-------------------------")
    else:
        print("Opps you reached 3 attempts and you are not the admin")
