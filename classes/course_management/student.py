##########################################################################
from datetime import date
from helpers import generate_id
##########################################################################
class Student:
    def __init__(self, first_name, last_name, birth_year, gender="male"):
        self.id = generate_id()
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.age = date.today().year - self.birth_year
        self.gender = gender
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
    def assign_courses(self, *courses):
        self.courses.extend(courses)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"""
Student Details:
----------------
    ID: {self.id}
    Name: {self.get_full_name()}
    Birth Year: {self.birth_year}
    Age: {self.age}
    Gender: {self.gender}
----------------
    """
    def __repr__(self):
        return f"{self.get_full_name()} is {self.gender} student and has {self.age} years old"
