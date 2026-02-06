################################################################################
from datetime import date
from helpers import generate_id
################################################################################
class Guest:
    def __init__(self, first_name, last_name, phone_number, birth_year, gender):
        self.id = generate_id()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.age = date.today().year - self.birth_year
        self.generation = self.get_generation()
        self.gender = gender

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

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.get_full_name()} is {self.gender} guest and has {self.age} years old"

    def __str__(self):
        return f"""
Guest Details:
----------------
    ID: {self.id}
    Name: {self.get_full_name()}
    Birth Year: {self.birth_year}
    Age: {self.age}
    Gender: {self.gender}
----------------
"""
