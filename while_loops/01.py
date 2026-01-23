# build an account login program:
# collect the user name and password
# if the password is "19011" print "welcome {user_name}"
# if the password is incorrect print "incorrect password try again"
# loop until the password is correct

print("account login program")
print("-------------------------")
user_name = input("Enter your name: ").upper()
password = input("Enter your password: ")
print("-------------------------")

while password != "19011":
    password = input("incorrect password try again: ")

print("-------------------------")
print(f"welcome {user_name}")
print("-------------------------")
