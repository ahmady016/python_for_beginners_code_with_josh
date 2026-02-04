# build a person class wih magic methods that hold:
# -------------------------------------------------
# person first name, last name, birth year, height, weight, gender and city
# and calculate the person's BMI based on weight and height
# and calculate the person's age based on the birth year
# and calculate the person's generation based on the person's age as:
# from 1965 to 1980 is [Gen X]
# and from 1981 to 1996 is [Gen Y]
# and from 1997 to 2012 is [Gen Z]
# and from 2013 to 2025 is [Gen Alpha]
# and from 2026 to 2039 is [Gen Beta]
# and print the person's full name, age, bmi, gender, city and generation
# and check if two persons are the same by comparing their gender,wight, height and birth year
###############################################################################
from datetime import date
###############################################################################
class Person:
    persons_count = 0
    def __init__(self, first_name, last_name, birth_year, height=175, weight=75, gender="male", city="cairo", bank_balance=0.0):
        Person.persons_count += 1
        self.id = Person.persons_count
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.height = height
        self.weight = weight
        self.gender = gender
        self.city = city
        self.bank_balance = bank_balance
        self.bio = self.__repr__()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_bmi(self):
        return self.weight / (self.height / 100) ** 2

    def get_age(self):
        return date.today().year - self.birth_year

    def get_generation(self):
        if self.birth_year >= 1965 and self.birth_year <= 1980:
            return "Gen X"
        elif self.birth_year >= 1981 and self.birth_year <= 1996:
            return "Gen Y"
        elif self.birth_year >= 1997 and self.birth_year <= 2012:
            return "Gen Z"
        elif self.birth_year >= 2013 and self.birth_year <= 2025:
            return "Gen Alpha"
        else:
            return "Gen Beta"

    def print_person_details(self):
        print(f"Person_#{self.id}_Details:")
        print("-------------------------")
        print(f"Full Name: {self.get_full_name()}")
        print(f"Birth Year: {self.birth_year}")
        print(f"Age: {self.get_age()}")
        print(f"Generation: {self.get_generation()}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
        print(f"BMI: {self.get_bmi():.2f}")
        print(f"Gender: {self.gender}")
        print(f"City: {self.city}")
        print(f"Bank Balance: {self.bank_balance}")
        print("-------------------------")

    def __repr__(self):
        return f"Person_#{self.id}: {self.first_name} {self.last_name} is {self.get_age()} years old and he is {self.gender} from {self.city} and has a money balance of {self.bank_balance}"
    def __str__(self):
        return f"""Person_#{self.id}_Details:
            Name: {self.get_full_name()}
            Gender: {self.gender}
            City: {self.city}
            BMI: {self.get_bmi():.2f}
            Age: {self.get_age()}
            Generation: {self.get_generation()}
            Bank Balance: {self.bank_balance}"""
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.gender == other.gender and self.birth_year == other.birth_year and self.height == other.height and self.weight == other.weight
        return False
    def __add__(self, other):
        if isinstance(other, Person):
            return self.bank_balance + other.bank_balance
        elif isinstance(other, int):
            return self.bank_balance + other
        elif isinstance(other, float):
            return self.bank_balance + other
        elif isinstance(other, str) and other.isdigit():
            return self.bank_balance + float(other)
        else:
            return self.bank_balance
##################################################################################
print("##################################")
print("Person Class Test Program Started")
print("##################################")
##################################################################################
omar = Person(
    first_name="Omar",
    last_name="Salah",
    birth_year=1992,
    height=175,
    weight=75,
    gender="male",
    city="cairo",
    bank_balance=25800
)
sayed = Person(
    first_name="Sayed",
    last_name="Aly",
    birth_year=2001,
    height=180,
    weight=88,
    gender="male",
    city="giza",
    bank_balance=14575
)
yasser = Person(
    first_name="yasser",
    last_name="Mohammed",
    birth_year=2001,
    height=180,
    weight=88,
    gender="male",
    city="giza",
    bank_balance=5500
)
persons_list = [omar, sayed, yasser]
print("----------------------------------")
print(f"number of persons: {Person.persons_count}")
print("----------------------------------")
print(omar)
print("----------------------------------")
print(sayed)
print("----------------------------------")
print(yasser)
print("----------------------------------")
print(f"does omar and sayed is the same? {omar == sayed}")
print("----------------------------------")
print(f"does omar and yasser is the same? {omar == yasser}")
print("----------------------------------")
print(f"does sayed and yasser is the same? {sayed == yasser}")
print("----------------------------------")
yasser.print_person_details()
print("----------------------------------")
print("Persons List:")
print("----------------------------------")
print(persons_list)
print("----------------------------------")
print("Persons Bio:")
print("----------------------------------")
print("\n".join(person.bio for person in persons_list))
print("----------------------------------")
print(f"omar + sayed = ${(omar + sayed):.2f}")
print("----------------------------------")
##################################################################################
print("##################################")
print("Person Class Test Program Finished")
print("##################################")
##################################################################################
