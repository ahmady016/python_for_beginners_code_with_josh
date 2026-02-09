################################################################################
from datetime import date
################################################################################
class PersonInfo:
    def __init__(self, first_name, last_name, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.gender = gender

        self.full_name = self.get_full_name()
        self.initials = self.get_initials()
        self.age = date.today().year - self.birth_year
        self.generation = self.get_generation()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"
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

    def __str__(self):
        return f"""
{self.initials} Details:
----------------
    Name: {self.full_name}
    Gender: {self.gender}
    Age: {self.age}
    Generation: {self.generation}
----------------
"""
    def __repr__(self):
        return f"Person('{self.first_name}', '{self.last_name}', {self.birth_year}, '{self.gender}')"
