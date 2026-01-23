# build a username checker program:
# collect the user name and username
# loop in every letter of the username
# and check if the username contains any invalid characters from "!@#$%^&*()+=-*/{}[]:;'<>,.?"
# then print "invalid username" and the invalid character
# otherwise if the username is correct print "welcome {user_name} your username is {username}"

print("username checker program")
print("-------------------------")
user_name = input("Enter your name: ").upper()
username = input("Enter your username: ")
print("-------------------------")

invalid_characters = "!@#$%^&*()+=-*/{}[]:;'<>,.? "
invalid_character = ""
for letter in username:
    if letter in invalid_characters:
        invalid_character = letter
        break

if invalid_character == "":
    print(f"welcome {user_name} your username is ({username})")
else:
    print(f"character {invalid_character} is invalid in your username")

