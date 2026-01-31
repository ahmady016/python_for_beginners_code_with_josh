# build a country guesser program as:
# first ask the user to enter his name
# then ask the user to enter a country
# while the input is not 0 add the country to a list
# once the user enter 0 ask the user to guess a country
# loop throw the countries list and check if the user guess is in the list
# if the user guess is in the list print "congrats you guessed the right country"
# if the user guess is not in the list print "try again you didn't guess the right country"
# if the user enter 0 print "Have a nice day"
#################################################
print("##########################")
print("country guesser program")
print("##########################")
#################################################
user_name = input("Enter your name: ").upper()
#################################################
countries = []
print("=========================")
user_country = input("Enter a country: ").capitalize()
while user_country != "0":
    countries.append(user_country)
    user_country = input("Enter a country: ").capitalize()
print("=========================")
#################################################
guess = input("please guess a country: ").capitalize()
if guess in countries:
    print("congrats you guessed the right country")
else:
    print("Sorry you didn't guess the right country")
#################################################
print("##########################")
print("Counties You Entered: ", countries)
print(f"Have a nice day {user_name}")
print("##########################")
