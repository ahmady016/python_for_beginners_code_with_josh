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
