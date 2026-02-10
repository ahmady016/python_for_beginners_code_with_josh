###############################################################################
from datetime import date
from helpers import generate_id
###############################################################################
class Customer:
    def __init__(self, first_name, last_name, address, phone_number, birth_year, gender):
        self.id = generate_id(12)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.gender = gender

        self.full_name = self.get_full_name()
        self.age = date.today().year - self.birth_year
        self.generation = self.get_generation()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
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

    def __repr__(self):
        return f"Customer('{self.first_name}', '{self.last_name}', '{self.address}', '{self.phone_number}', {self.birth_year}, '{self.gender}')"
    def __str__(self):
        return f"""-------------------
    Name: {self.first_name} {self.last_name}
    Address: {self.address}
    Phone Number: {self.phone_number}
    Age: {self.age}
    Generation: {self.generation}
----------------------"""
