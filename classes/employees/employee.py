########################################################################################
from person_info import PersonInfo
from qualification_info import QualificationInfo
from contact_info import ContactInfo
########################################################################################
class Employee(PersonInfo, ContactInfo, QualificationInfo):
    def __init__(self, first_name, last_name, birth_year, gender, address, phone_number, email, grade_name, grade_year, grade_percentage, hire_date, job_title, department, salary):
        PersonInfo.__init__(self, first_name, last_name, birth_year, gender)
        ContactInfo.__init__(self, address, phone_number, email)
        QualificationInfo.__init__(self, grade_name, grade_year, grade_percentage)

        self.hire_date = hire_date
        self.job_title = job_title
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"""
Employee Details:
----------------
    Name: {self.get_full_name()}
    Gender: {self.gender}
    Age: {self.age}
    Generation: {self.generation}
    Address: {self.address}
    Phone Number: {self.phone_number}
    Email: {self.email}
    Qualification: {self.grade_name}, {self.grade_year}, {self.grade_percentage}
    Hire Date: {self.hire_date}
    Job Title: {self.job_title}
    Department: {self.department}
    Salary: {self.salary}
----------------
"""
    def __repr__(self):
        return f"{self.get_full_name()} is {self.gender} employee and has {self.age} years old and he is {self.generation} generation and work as {self.job_title} in {self.department}"

