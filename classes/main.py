# build some classes to demonstrate:
# ---------------------------------
# mangled fields with setter and getter and computed readonly properties
####################################################################################
class BankAccount:
    def __init__(self, owner_name, initial_balance=500.0):
        ### mangled internal fields
        self.__owner_name = owner_name
        self.__balance = initial_balance

    @property
    def owner_name(self):
        ### safe way for getting the backing field __owner_name
        return self.__owner_name
    @owner_name.setter
    def owner_name(self, value):
        ### intercepts setting the balance property to perform validation
        if not isinstance(value, str):
            raise TypeError("Owner name must be a string")
        if len(value) < 5:
            raise ValueError("Owner name must be at least 5 characters")
        if len(value) > 40:
            raise ValueError("Owner name cannot exceed 40 characters")
        ### update the mangled field __owner_name if the value is valid
        self.__owner_name = value

    @property
    def balance(self):
        ### safe way for getting the backing field __balance
        return self.__balance
    @balance.setter
    def balance(self, value):
        ### intercepts setting the balance property to perform validation
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be a number")
        if value < 0.0:
            raise ValueError("Balance cannot be negative")
        if value > 1000000.0:
            raise ValueError("Balance cannot exceed 1,000,000 in one time assignment")
        ### update the mangled field __balance if the value is valid
        self.__balance = value

    def __repr__(self):
        return f"BankAccount(owner='{self.owner_name}', balance={self.balance})"
####################################################################################
class Hotel:
    PROPERTY_TYPES = ["Hotel", "Apartment", "Motel", "Resort", "Guesthouse", "Boutique"]
    def __init__(self, name, property_type, room_rate=50.0, nights=1):
        self.__name = name
        self.__property_type = property_type
        self.__room_rate = room_rate
        self.__nights = nights
        self.__tax_rate = 0.05

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 5:
            raise ValueError("Name must be at least 5 characters")
        if len(value) > 40:
            raise ValueError("Name cannot exceed 40 characters")
        ### update the mangled field __name if the value is valid
        self.__name = value

    @property
    def property_type(self):
        return self.__property_type
    @property_type.setter
    def property_type(self, value):
        if not isinstance(value, str):
            raise TypeError("Property type must be a string")
        if value not in Hotel.PROPERTY_TYPES:
            raise ValueError(f"Property type must be one of {Hotel.PROPERTY_TYPES}")
        ### update the mangled field __property_type if the value is valid
        self.__property_type = value

    @property
    def room_rate(self):
        return self.__room_rate
    @room_rate.setter
    def room_rate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Room rate must be a number")
        if value < 0.0:
            raise ValueError("Room rate cannot be negative")
        if value < 20.0:
            raise ValueError("Room rate cannot be less than $10 per night")
        if value > 1200.0:
            raise ValueError("Room rate cannot exceed $1,200 per night")
        ### update the mangled field __room_rate if the value is valid
        self.__room_rate = value

    @property
    def nights(self):
        return self.__nights
    @nights.setter
    def nights(self, value):
        if not isinstance(value, int):
            raise TypeError("Nights must be an integer")
        if value < 1:
            raise ValueError("Nights cannot be less than 1")
        if value > 60:
            raise ValueError("Nights cannot exceed 60")
        ### update the mangled field __nights if the value is valid
        self.__nights = value

    @property
    def base_cost(self):
        return self.room_rate * self.nights
    @property
    def tax_amount(self):
        return round(self.base_cost * self.__tax_rate, 2)
    @property
    def total_cost(self):
        return round(self.base_cost + self.tax_amount, 2)
    @property
    def average_cost(self):
        return round(self.total_cost / self.nights, 2)

    def __repr__(self):
        return f"Hotel({self.name}, {self.property_type}, {self.room_rate}, {self.nights})"
####################################################################################
# test the BankAccount class
####################################################################################
print("########################")
print("BankAccount Class Test")
print("########################")
# create a bank account
ahmed_account = BankAccount("Ahmed")
# set the owner name and balance with valid values
ahmed_account.owner_name = "Ahmed Mohammad Abdulrahman"
ahmed_account.balance = 5000
# print the owner name and balance
print("------------------------")
print(f"Owner Name: {ahmed_account.owner_name}")
print(f"Balance: {ahmed_account.balance}")
print("------------------------")

# set the balance with invalid values
print("Invalid balance values")
print("------------------------")
try:
    ahmed_account.balance = "5000"
except Exception as error:
    print(error)
try:
    ahmed_account.balance = 1000001
except Exception as error:
    print(error)
try:
    ahmed_account.balance = -100
except Exception as error:
    print(error)
print("------------------------")

# set the owner name with invalid values
print("Invalid owner name values")
print("------------------------")
try:
    ahmed_account.owner_name = 0
except Exception as error:
    print(error)
try:
    ahmed_account.owner_name = "AAM"
except Exception as error:
    print(error)
try:
    ahmed_account.owner_name = "Ahmed Abdulrahman Mohammad Ahmed Abdulrahman Mohammad"
except Exception as error:
    print(error)

# print the owner name and balance
print("------------------------")
print(ahmed_account)
print("------------------------")
####################################################################################
# test the Hotel class
####################################################################################
print("########################")
print("Hotel Class Test")
print("########################")
# create a hotel
raya_hotel = Hotel("Raya", "resort")
# set the hotel name and property type with valid values
raya_hotel.name = "Raya Resort and Spa"
raya_hotel.property_type = "Resort"
raya_hotel.room_rate = 250
raya_hotel.nights = 10

# print the hotel name and property type and room rate and nights
print("------------------------")
print(f"Hotel Name: {raya_hotel.name}")
print(f"Property Type: {raya_hotel.property_type}")
print(f"Room Rate: {raya_hotel.room_rate}")
print(f"Nights: {raya_hotel.nights}")
print("------------------------")

# set the property type with invalid values
print("Invalid property type values")
print("------------------------")
try:
    raya_hotel.property_type = None
except Exception as error:
    print(error)
try:
    raya_hotel.property_type = "Resort and Spa"
except Exception as error:
    print(error)
print("------------------------")

# set the hotel name with invalid values
print("Invalid hotel name values")
print("------------------------")
try:
    raya_hotel.name = None
except Exception as error:
    print(error)
try:
    raya_hotel.name = "Raya"
except Exception as error:
    print(error)
try:
    raya_hotel.name = "Raya Resort and Spa and Spa Raya Resort and Spa and Spa Raya Resort and Spa and Spa"
except Exception as error:
    print(error)
print("------------------------")

# test the nights with invalid values
print("Invalid nights values")
print("------------------------")
try:
    raya_hotel.nights = 0
except Exception as error:
    print(error)
try:
    raya_hotel.nights = 61
except Exception as error:
    print(error)
print("------------------------")

# print the hotel name and property type and room rate and nights
print("------------------------")
print(raya_hotel)
print("------------------------")

# test the computed properties
print("------------------------")
print(f"Base Cost: {raya_hotel.base_cost}")
print(f"Tax Amount: {raya_hotel.tax_amount}")
print(f"Total Cost: {raya_hotel.total_cost}")
print(f"Average Cost: {raya_hotel.average_cost}")
print("------------------------")
