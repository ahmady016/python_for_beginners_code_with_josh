########################################################################################
from datetime import date
from helpers import generate_id
########################################################################################
class Customer:
    def __init__(self, first_name, last_name, address, birth_year, gender):
        self.id = generate_id(8)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.birth_year = birth_year
        self.gender = gender

        self.full_name = f"{self.first_name} {self.last_name}"
        self.age = date.today().year - self.birth_year
        self.generation = self.get_generation()

    def get_generation(self):
        if self.birth_year <= 1980:
            return "Gen X"
        elif self.birth_year <= 1997:
            return "Gen Y"
        elif self.birth_year <= 2012:
            return "Gen Z"
        elif self.birth_year <= 2025:
            return "Gen Alpha"
        else:
            return "Gen Beta"

    def __repr__(self):
        return f"{self.full_name} is {self.gender} customer and lives in {self.address} and has {self.age} years old and is {self.generation} generation"
    def __str__(self):
        return self.__repr__()
