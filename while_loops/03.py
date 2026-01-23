# build a number one programming language guesser program:
# collect the user's name and number one programming language guess
# the user have only 5 times tries to guess the right programming language [python]
# if the user guess the right programming language print "congrats {user_name} you guessed the right programming language in 1 tries"
# if the user does not guess the right programming language print "try again {user_name} you have only 4 tries left"

print("number one programming language guesser program")
print("------------------------------------------------")
user_name = input("Enter your name: ").upper()
guess = input("Enter your guess: ").lower()
print("------------------------------------------------")

MAX_TRIES = 5
tries = 1
while tries < MAX_TRIES and guess != "python":
    guess = input(f"try again {user_name} you have only {MAX_TRIES - tries} tries left: ")
    print("------------------------------------------------")
    tries += 1

if guess == "python":
    print(f"congrats {user_name} you guessed the right programming language in {tries} tries")
else:
    print(f"Sorry {user_name} you did not guess the right programming language in 5 tries")
print("------------------------------------------------")
