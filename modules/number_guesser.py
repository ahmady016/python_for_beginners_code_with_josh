# build a number guesser program using the random module as:
# generate a random number between 1 and 100
# ask the user to enter a number between 1 and 100
# collect the user's name and count the user guesses
# check if the user guess is lower to the random number print "Too Low, try again"
# check if the user guess is higher to the random number print "Too High, try again"
# if the user guess is equal to the random number print "Congratulations You guessed the right number"

from random import randint

print("number guesser program")
print("----------------------")
###############################################################
winning_number = randint(1, 100)
user_name = input("Enter your name: ").upper()
user_number = int(input("Enter a number between 1 and 100: "))
guess_count = 1
################################################################
while user_number != winning_number:
    print("-------------------------")
    if user_number > winning_number:
        print("Too High, try again")
    else:
        print("Too Low, try again")
    user_number = int(input("Enter a number between 1 and 100: "))
    guess_count += 1
################################################################
print(f"Congratulations {user_name}, You guessed the right number in #{guess_count} tries")
print("----------------------")

print("Number Guesser Program Completed Successfully")
print("----------------------")
