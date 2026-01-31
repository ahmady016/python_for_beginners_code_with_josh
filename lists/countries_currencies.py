# build a countries and their currencies program as:
# collect the user name
# create an empty dictionary
# and ask the user to enter a country and its currency separated by a space
# then update the dictionary with the country and its currency
# loop until the user enter 0 to quit
# at the end print the countries and their currencies
#################################################
print("####################")
print("countries currencies")
print("####################")
#################################################
user_name = input("Enter your name: ").upper()
print("----------------------------------------")
#################################################
countries_with_currencies = {
    "Egypt": "Egyptian Pound",
    "Saudi Arabia": "Saudi Riyal"
}
user_response = input("Enter a country and its currency separated by a space: ")
while user_response != "0":
    (country, currency) = user_response.split(" ")
    if country in countries_with_currencies:
        print(f"Sorry {country} is already in the list")
        continue
    if country != "0":
        countries_with_currencies[country] = currency
    user_response = input("Enter a country and its currency separated by a space: ")
#################################################
print("----------------------------------------")
print(f"Hi {user_name}, the countries and their currencies are:")
print("----------------------------------------")
for country, currency in countries_with_currencies.items():
    print(f"{country}'s currency is {currency}")
#################################################
print("####################")
print("countries currencies completed successfully")
print("####################")
#################################################
