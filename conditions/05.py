# build a python learning recommendation program:
# collect the user's name
# ask the user if he want to read a book [yes/no]
# if the user wants to read a book recommend ask him his current level [beginner, intermediate, advanced]
# if the current level is beginner recommend [Python Crash Course] book
# if the current level is intermediate recommend [Python - Automate the boring stuff] book
# if the current level is advanced recommend [Data Structures and Algorithms in Python] book
# if the user does not want to read a book recommend [Python Course for Beginners - Code With Josh] video

print("python learning recommendation program")
print("--------------------------------------")
user_name = input("Enter your name: ").upper()
want_to_read_book = input("Do you want to read a book? [yes/no]: ").lower()

if want_to_read_book == "yes":
    current_level = input("Enter your current level [beginner, intermediate, advanced]: ").lower()
    print("--------------------------------------")
    if current_level == "beginner":
        print(f"Hi {user_name}, you should read (Python Crash Course) book")
    elif current_level == "intermediate":
        print(f"Hi {user_name}, you should read (Python - Automate the boring stuff) book")
    elif current_level == "advanced":
        print(f"Hi {user_name}, you should read (Data Structures and Algorithms in Python) book")
    else:
        print(f"Hi {user_name} you entered invalid level")
else:
    print("--------------------------------------")
    print(f"Hi {user_name}, you should watch (Python Course for Beginners - Code With Josh) youtube video")

print("--------------------------------------")
