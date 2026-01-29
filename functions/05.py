# build an adventure planning program:
# that ask the user to enter 1 to start and loops tell the user enter 0 to quit
# in the program ask the user if he has destination [yes/no]
# if the user has destination then plan the adventure transport [Car, Train, Flight]
# otherwise aide the user to choose a destination asking for the kind of trip [beach, city, mountains]

###################################################################
def car_transport():
    print("Road trips are fun")
    people_number = int(input("Enter the number of people: "))
    if people_number > 4:
        print("You should rent a van with $600 per day or microbus with $900 per day")
    else:
        print("Great you can rent a car with $400 per day")
###################################################################
def train_transport():
    seat_class = input("Enter the seat class [economy, business, vip]: ").lower()
    if seat_class == "vip":
        print("Great more comfort in your way and Your ticket price is $150")
    elif seat_class == "business":
        print("Great more comfort in your way and Your ticket price is $100")
    else:
        print("You save some money and your ticket price is $50")
###################################################################
def plane_transport():
    class_type = input("Enter the class type [economy, business, first]: ").lower()
    luggage_weight = float(input("Enter the baggage weight in kg: "))
    if luggage_weight > 20 and class_type == "business" or class_type == "first":
        print("Great you can have more luggage with this class and your ticket price is $200")
    elif luggage_weight <= 20 and class_type == "business" or class_type == "first":
        print("You can bring more luggage with this class and your ticket price is $150")
    else:
        print("You may have too much luggage and your ticket price is $100")
###################################################################
def mountains_trip():
    activity = input("Enter the activity [camping, hiking]: ").lower()
    if activity == "camping":
        print("Check out the many camping sites in Yosemite")
    elif activity == "hiking":
        print("Try hiking Half Dome")
    else:
        print("We don't have this mountains activity")
###################################################################
def city_trip():
    activity = input("Enter the activity [shopping, sightseeing]: ").lower()
    if activity == "shopping":
        print("Check out the city mall")
    elif activity == "sightseeing":
        print("Check out the city museum")
    else:
        print("We don't have this city activity")
###################################################################
def beach_trip():
    beach_type = input("Enter the type of beach [sandy, rocky]: ").lower()
    if beach_type == "sandy":
        print("Check out Waiheke beach")
    elif beach_type == "rocky":
        print("Head over to the North Shore")
    else:
        print("We don't have this type of beach")
###################################################################
print("adventure planning program")
print("--------------------------")
###################################################################
user_name = input("Enter your name: ").upper()
start = int(input("Enter 1 to start and 0 to quit: "))
print("--------------------------------------")

while start == 1:
    has_destination = input("Do you have a destination? [yes/no]: ").lower()
    if has_destination == "yes":
        print("let's plan your adventure:")
        print("--------------------------")

        transport = input("Enter the transport [car, train, plane]: ").lower()
        print("--------------------------------------")
        if transport == "car":
            car_transport()
        elif transport == "train":
            train_transport()
        elif transport == "plane":
            plane_transport()
        else:
            print("We don't have this transport")
    else:
        print("let's choose your destination:")
        print("------------------------------")
        trip_type = input("Enter the trip type [beach, city, mountains]: ").lower()
        print("--------------------------------------")
        if trip_type == "beach":
            beach_trip()
        elif trip_type == "city":
            city_trip()
        elif trip_type == "mountains":
            mountains_trip()
        else:
            print("That trip type is not available")

    start = int(input("Enter 1 to start and 0 to quit: "))
    print("--------------------------------------")

print("Have fun on your trip")
print("--------------------------------------")
