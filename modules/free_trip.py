# build a free trip program using the random module as:
# generate the winning number between 1 and 100
# ask the user to enter his name and a number between 1 and 100
# if the user guess equal the winning number print "Congratulations You win a free trip"
# otherwise print "Opps, You didn't win a free trip!"

from random import randint

print("free trip program")
print("-------------------------")
winning_number = randint(1, 100)
user_name = input("Enter your name: ").upper()
user_number = int(input("Enter a number between 1 and 100: "))
print("-------------------------")

if user_number == winning_number:
    print(f"Congratulations {user_name}, You win a free trip")
else:
    print(f"Opps {user_name}, You didn't win a free trip")

print("Free Trip Program Completed Successfully")
print("-------------------------")
