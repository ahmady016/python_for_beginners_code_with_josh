# build a mobile number checker program:
# collect the user's name and mobile number
# check if the mobile number length is 11 and if not print "invalid mobile number"
# loop in every letter of the mobile number
# and check if the mobile number contains any other characters than "+0123456789"
# then print "invalid mobile number" and the invalid character

valid_characters = "+0123456789"
print("mobile number checker program")
print("-------------------------")
user_name = input("Enter your name: ").upper()
mobile_number = input("Enter your mobile number: ")
print("-------------------------")

if len(mobile_number) != 11:
    print(f"Opps {user_name} you must enter 11 digits mobile number")
else:
    invalid_character = ""
    for letter in mobile_number:
        if letter not in valid_characters:
            invalid_character = letter
            break

    if invalid_character == "":
        print(f"welcome {user_name} your mobile number is ({mobile_number})")
    else:
        print(f"character {invalid_character} is invalid in your mobile number")

    print("-------------------------")
