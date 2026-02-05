##########################################################################
from instructor import Instructor
from student import Student
from helpers import generate_id
##########################################################################
class Course:

    def __init__(self, title, description, total_hours):
        self.id = generate_id()
        self.title = title
        self.description = description
        self.total_hours = total_hours
        self.current_instructor = None
        self.students = {}

    def assign_instructor(self, instructor: Instructor):
        if isinstance(instructor, Instructor):
            self.current_instructor = instructor
        else:
            print(f"this is not an instructor")

    def enroll_student(self, student: Student):
        if not isinstance(student, Student):
            print(f"this is not a student")
        elif student.id in self.students.keys():
            print(f"{student.get_full_name()} is already enrolled in this course")
        else:
            self.students[student.id] = { "student": student, "score": None, "completed": False }
    def enroll_students(self, *students: Student):
        for student in students:
            self.enroll_student(student)

    def assign_score(self, student, score):
        if not isinstance(student, Student):
            print(f"this is not a student")
        elif student.id not in self.students.keys():
            print(f"{student.get_full_name()} is not enrolled in this course")
        if score < 0 or score > 100:
            print(f"Score must be between 0 and 100")
        else:
            self.students[student.id]["score"] = score
    def mark_completed(self, student: Student):
        if not isinstance(student, Student):
            print(f"this is not a student")
        elif student.id not in self.students.keys():
            print(f"{student.get_full_name()} is not enrolled in this course")
        else:
            self.students[student.id]["completed"] = True
    def average_score(self):
        scores = [student["score"] for student in self.students.values() if student["score"] != None]
        return 0 if len(scores) == 0 else round(sum(scores) / len(scores), 2)

    def __str__(self):
        return f"""
Course Details:
------------------------------------------------------------
    ID: {self.id}
    Title: {self.title}
    Description: {self.description}
    Total Hours: {self.total_hours} hours
    Instructor: {self.current_instructor.get_full_name() if self.current_instructor else "No Instructor"}
    Students: {
        "No Students Enrolled" if len(self.students.keys()) == 0 else "\n\t".join([student["student"].get_full_name() for student in self.students.values()])
    }
------------------------------------------------------------
"""
    def __repr__(self):
        return f"{self.title} - {self.description} - {self.total_hours} hours"
