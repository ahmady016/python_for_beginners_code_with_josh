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
    ### class fields (counter) ###
    persons_count = 0
    ### class constructor ###
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

        ### public fields (computed properties) ### can be accessed from outside
        self.bio = self.__repr__()
        self.details = self.__str__()
        ### private fields (used by setter and getter) ### can not be accessed from outside
        self.__full_name = self.full_name
        self.__generation = self.generation
        self.__age = self.age
        self.__bmi = self.bmi

    ### setter and getter for backing fields ###
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def bmi(self):
        return self.weight / (self.height / 100) ** 2
    @bmi.setter
    def bmi(self, value):
        self.__bmi = value

    @property
    def generation(self):
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
    @generation.setter
    def generation(self, value):
        self.__generation = value

    @property
    def age(self):
        return date.today().year - self.birth_year
    @age.setter
    def age(self, value):
        self.__age = value

    ### class methods ###
    def print_details(self):
        print(f"Person_#{self.id}_Details:")
        print("-------------------------")
        print(f"Full Name: {self.full_name}")
        print(f"Birth Year: {self.birth_year}")
        print(f"Generation: {self.generation}")
        print(f"Age: {self.age}")
        print(f"BMI: {self.bmi:.2f}")
        print(f"Gender: {self.gender}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
        print(f"City: {self.city}")
        print(f"Bank Balance: {self.bank_balance}")
        print("-------------------------")

    def __repr__(self):
        return f"Person_#{self.id}: {self.full_name} is {self.age} years old and he is {self.gender} from {self.city} and has a money balance of {self.bank_balance}"
    def __str__(self):
        return f"""Person_#{self.id}_Details:
            Name: {self.full_name}
            Generation: {self.generation}
            Age: {self.age}
            BMI: {self.bmi:.2f}
            Gender: {self.gender}
            City: {self.city}
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
print("omar details: using the mangled backing fields")
print("----------------------------------")
print(f"omar name: {omar._Person__full_name}")
print(f"omar generation: {omar._Person__generation}")
print(f"omar age: {omar._Person__age}")
print(f"omar bmi: {omar._Person__bmi:.2f}")
print("----------------------------------")
print(sayed.__repr__())
print("----------------------------------")
print(f"does omar and sayed is the same? {omar == sayed}")
print("----------------------------------")
print(f"does omar and yasser is the same? {omar == yasser}")
print("----------------------------------")
print(f"does sayed and yasser is the same? {sayed == yasser}")
print("----------------------------------")
yasser.print_details()
print("----------------------------------")
print("Persons details:")
print("----------------------------------")
print("\n".join([person.details for person in persons_list]))
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
