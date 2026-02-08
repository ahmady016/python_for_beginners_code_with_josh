# build a Hotel Management System using oop approach that allows admin to:
# ------------------------------------------------------------------------
# add a hotel with name, location, capacity, rooms and type
# the hotel types are [resort, hotel, boutique, economy]
# add a new guest with first name, last name, phone number, birth year, gender
# and calculate the guest's rank based on volume(total_nights) and value (total_spent)
# and there is a ranking formula for each hotel type [resort, hotel, boutique, economy]
# as follows:
# resort: rank = total_nights * 5 + total_spent / 5
# hotel: rank = total_nights * 25 + total_spent / 50
# boutique: rank = total_nights * 15 + total_spent / 15
# economy: rank = total_nights * 50 + total_spent / 100
# and based on the guest's rank (Weight) he assigned a guest tier [bronze, silver, gold, platinum] as follows:
# bronze: if the rank is less than 100
# silver: if the rank is between 100 and 250
# gold: if the rank is between 250 and 500
# platinum: if the rank is more than 500
# the system should add the guest to the guest list in each hotel
# and calculate the the guest rank and tier
# then finally sort the guests in each hotel by their rank
# and the admin can view the guest list in each hotel with guest details [name, phone number, rank, tier]
# and the admin can view the guest list in each hotel by tier
###############################################################################
from guest import Guest
from hotel import Hotel
###############################################################################
print("##################################")
print("Welcome to Hotel Management System")
print("##################################")
###############################################################################
guest_01 = Guest("Ahmed", "Ali", "01143680055", 1985, "Male")
guest_02 = Guest("Mohammed", "Salah", "01121956787", 1995, "Male")
guest_03 = Guest("Hossam", "Adel", "01104525678", 1988, "Male")
guest_04 = Guest("Ramy", "Mohamed", "01002445675", 1991, "Male")
guest_05 = Guest("Abdallah", "Fawzy", "01023456789", 1984, "Male")

guest_06 = Guest("Reham", "Mahmoud", "01143680055", 1992, "Female")
guest_07 = Guest("Yasmin", "Roshdy", "01121956787", 1994, "Female")
guest_08 = Guest("Aya", "Aly", "01104525678", 1997, "Female")
guest_09 = Guest("Emad", "Amr", "01002445675", 1987, "Male")
guest_10 = Guest("Ahmed", "Shokry", "01023456789", 2002, "Male")

guest_11 = Guest("Hossam", "Hamdy", "01143680055", 2000, "Male")
guest_12 = Guest("Sayed", "Gaber", "01121956787", 1975, "Male")
guest_13 = Guest("Ghana", "Emam", "01104525678", 2003, "Female")
guest_14 = Guest("Gaber", "Yasser", "01002445675", 1999, "Male")
guest_15 = Guest("Rabab", "Sayed", "01023456789", 1993, "Female")

guest_16 = Guest("Soliman", "Zakaria", "01143680055", 1988, "Male")
guest_17 = Guest("Yousef", "Abdelaziz", "01121956787", 1982, "Male")
guest_18 = Guest("Waleed", "Mohamed", "01104525678", 1997, "Male")
guest_19 = Guest("Yasser", "Zakaria", "01002445675", 1998, "Male")
guest_20 = Guest("Ramy", "Ramadan", "01023456789", 2002, "Male")
###############################################################################
hotel_01 = Hotel("Ocean Resort", "Sharm ElSheikh", 100, 80, "Resort")
hotel_02 = Hotel("Grand Hotel", "Cairo", 100, 150, "Hotel")
hotel_03 = Hotel("Birds Boutique", "Alex", 30, 60, "Boutique")
hotel_04 = Hotel("Oraby Economy", "Fayoum", 12, 24, "Economy")
###############################################################################
hotel_01.add_guest_details(guest_01, 5, 1250)
hotel_01[guest_01.id] = { "nights": 3, "spent": 750 }

hotel_01.add_guest_details(guest_02, 3, 900)
hotel_01[guest_02.id] = { "nights": 7, "spent": 1950 }

hotel_01.add_guest_details(guest_03, 10, 3000)
hotel_01.add_guest_details(guest_04, 15, 9500)
hotel_01.add_guest_details(guest_05, 20, 7500)
###############################################################################
hotel_02.add_guest_details(guest_06, 5, 750)
hotel_02[guest_06.id] = { "nights": 7, "spent": 1150 }

hotel_02.add_guest_details(guest_07, 3, 450)
hotel_02[guest_07.id] = { "nights": 5, "spent": 900 }

hotel_02.add_guest_details(guest_08, 10, 1250)
hotel_02[guest_08.id] = { "nights": 7, "spent": 1600 }

hotel_02.add_guest_details(guest_09, 15, 1750)
hotel_02[guest_09.id] = { "nights": 5, "spent": 875 }

hotel_02.add_guest_details(guest_10, 20, 2250)
###############################################################################
hotel_03.add_guest_details(guest_11, 5, 375)
hotel_03[guest_11.id] = { "nights": 3, "spent": 275 }

hotel_03.add_guest_details(guest_12, 3, 275)
hotel_03[guest_12.id] = { "nights": 7, "spent": 675 }

hotel_03.add_guest_details(guest_13, 10, 900)
hotel_03[guest_13.id] = { "nights": 3, "spent": 250 }

hotel_03.add_guest_details(guest_14, 15, 1350)
hotel_03.add_guest_details(guest_15, 20, 1850)
###############################################################################
hotel_04.add_guest_details(guest_16, 5, 350)
hotel_04[guest_16.id] = { "nights": 7, "spent": 650 }

hotel_04.add_guest_details(guest_17, 3, 650)
hotel_04.add_guest_details(guest_18, 10, 850)

hotel_04.add_guest_details(guest_19, 15, 1250)
hotel_04[guest_19.id] = { "nights": 5, "spent": 475 }

hotel_04.add_guest_details(guest_20, 20, 2000)
###############################################################################
print("-------------------------")
print(guest_01)
print(guest_07)
print(guest_13)
print("-------------------------")
###############################################################################
print("-------------------------")
print(hotel_01)
print("-------------------------")
print(hotel_01[guest_01.id])
print("-------------------------")

print("Average Guests Info:")
print("-------------------------")
print(f"Average Guests Age: {hotel_01.get_average_guests_age()}")
print(f"Average Guests Nights: {hotel_01.get_average_guests_nights()}")
print(f"Average Guests Spent: {hotel_01.get_average_guests_spent()}")
print(f"Average Guests Score: {hotel_01.get_average_guests_score()}")
print("-------------------------")

print("All Guests Info:")
print("-------------------------")
all_guests_info = hotel_01.get_all_guests_info()
print("\n".join(all_guests_info))
print("-------------------------")

print("Sorted Guests:")
print("-------------------------")
sorted_guests = hotel_01.get_sorted_guests_info()
print("\n".join(sorted_guests))
print("-------------------------")

print("Top 3 Guests Info:")
print("-------------------------")
top3_guests_info = hotel_01.get_top_scored_guests_info(3)
print("\n".join(top3_guests_info))
print("-------------------------")

print("All Bronze Guests Info:")
print("-------------------------")
all_bronze_guests_info = hotel_01.get_all_guests_info_by_tier("Bronze")
print("\n".join(all_bronze_guests_info))
print("-------------------------")

print("All Silver Guests Info:")
print("-------------------------")
all_silver_guests_info = hotel_01.get_all_guests_info_by_tier("Silver")
print("\n".join(all_silver_guests_info))
print("-------------------------")

print("All Gold Guests Info:")
print("-------------------------")
all_gold_guests_info = hotel_01.get_all_guests_info_by_tier("Gold")
print("\n".join(all_gold_guests_info))
print("-------------------------")

print("All Platinum Guests Info:")
print("-------------------------")
all_platinum_guests_info = hotel_01.get_all_guests_info_by_tier("Platinum")
print("\n".join(all_platinum_guests_info))
print("-------------------------")
###############################################################################
print("-------------------------")
print(hotel_02)
print("-------------------------")
print(hotel_02[guest_08.id])
print("-------------------------")

print("All Guests Info:")
print("-------------------------")
all_guests_info = hotel_02.get_all_guests_info()
print("\n".join(all_guests_info))
print("-------------------------")

print("All Silver Guests Info:")
print("-------------------------")
all_silver_guests_info = hotel_02.get_all_guests_info_by_tier("Silver")
print("\n".join(all_silver_guests_info))
print("-------------------------")

print("All Gold Guests Info:")
print("-------------------------")
all_gold_guests_info = hotel_02.get_all_guests_info_by_tier("Gold")
print("\n".join(all_gold_guests_info))
print("-------------------------")
###############################################################################
print("-------------------------")
print(hotel_03)
print("-------------------------")
print(hotel_03[guest_13.id])
print("-------------------------")

print("All Guests Info:")
print("-------------------------")
all_guests_info = hotel_03.get_all_guests_info()
print("\n".join(all_guests_info))
print("-------------------------")

print("All Bronze Guests Info:")
print("-------------------------")
all_bronze_guests_info = hotel_03.get_all_guests_info_by_tier("Bronze")
print("\n".join(all_bronze_guests_info))
print("-------------------------")

print("All Silver Guests Info:")
print("-------------------------")
all_silver_guests_info = hotel_03.get_all_guests_info_by_tier("Silver")
print("\n".join(all_silver_guests_info))
print("-------------------------")
###############################################################################
print("-------------------------")
print(hotel_03)
print("-------------------------")
print(hotel_03[guest_13.id])
print("-------------------------")

print("All Guests Info:")
print("-------------------------")
all_guests_info = hotel_03.get_all_guests_info()
print("\n".join(all_guests_info))
print("-------------------------")

print("All Bronze Guests Info:")
print("-------------------------")
all_bronze_guests_info = hotel_03.get_all_guests_info_by_tier("Bronze")
print("\n".join(all_bronze_guests_info))
print("-------------------------")

print("All Silver Guests Info:")
print("-------------------------")
all_silver_guests_info = hotel_03.get_all_guests_info_by_tier("Silver")
print("\n".join(all_silver_guests_info))
print("-------------------------")
###############################################################################
print("-------------------------")
print(hotel_04)
print("-------------------------")
print(hotel_04[guest_16.id])
print("-------------------------")

print("All Guests Info:")
print("-------------------------")
all_guests_info = hotel_04.get_all_guests_info()
print("\n".join(all_guests_info))
print("-------------------------")

print("All Gold Guests Info:")
print("-------------------------")
all_gold_guests_info = hotel_04.get_all_guests_info_by_tier('Gold')
print("\n".join(all_gold_guests_info))
print("-------------------------")

print("All Silver Guests Info:")
print("-------------------------")
all_silver_guests_info = hotel_04.get_all_guests_info_by_tier('Silver')
print("\n".join(all_silver_guests_info))
print("-------------------------")
###############################################################################
