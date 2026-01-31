# build a cities sort and list program as:
# collect the user name
# then ask the user to enter a city, until the user enter 0
# if the city is not in the list, add the city to the list
# otherwise print the city is already in the list
# once the user enter 0, sort the cities in alphabetical order and print the sorted cities
#################################################
print("############################")
print("cities sort and list program")
print("############################")
#################################################
print("----------------------------")
user_name = input("Enter your name: ").upper()
print("----------------------------")
#################################################
cities = []
city = ""
while city != "0":
    city = input("Enter a city: ").capitalize()
    if city == "0":
        break
    if city not in cities:
        cities.append(city)
    else:
        print(city, "is already in the list! try again")
#################################################
cities.sort()
print("========================")
print(f"Hi {user_name}, your entered #{len(cities)} cities and these are your sorted cities:")
for city in cities:
    print(city)
print("========================")
#################################################
