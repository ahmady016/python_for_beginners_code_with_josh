# build an online course management program using classes:
# --------------------------------------------------------
# admin can track courses, instructors, students and their grades
# it allow admin to see course details
# and assign an instructor to a course
# and enroll students to a course
# and assign a score to a student in a course
# and calculate the average scores of enrolled students in a course
# and mark a student as completed a course
########################################################################
from instructor import Instructor
from student import Student
from course import Course
########################################################################
print("##########################################")
print("course management program started")
print("##########################################")
#######################################################################################
# instructors
#######################################################################################
instructor_01 = Instructor("Omar", "Salah", 1990, "male", 5000)
instructor_02 = Instructor("Ahmed", "Adel", 1992, "male", 6000)
instructor_03 = Instructor("Yasser", "Abdallah", 1985, "male", 7000)
instructor_04 = Instructor("Mohammed", "Ali", 1988, "male", 4500)
instructor_05 = Instructor("Eman", "Mostafa", 1997, "female", 8700)
#######################################################################################
# students
#######################################################################################
student_01 = Student("Yousef", "Abdelaziz", 2001, "male")
student_02 = Student("Waleed", "Mohamed", 2004, "male")
student_03 = Student("Yasser", "Zakaria", 2003, "male")
student_04 = Student("Ramy", "Ramadan", 2000, "male")
student_05 = Student("Yasmin", "Roshdy", 2002, "female")
student_06 = Student("Aya", "Aly", 2005, "female")
student_07 = Student("Emad", "Amr", 1993, "male")
student_08 = Student("Ahmed", "Shokry", 1997, "male")
student_09 = Student("Hossam", "Hamdy", 1996, "male")
student_10 = Student("Sayed", "Gaber", 1980, "male")
student_11 = Student("Ghana", "Emam", 1987, "female")
student_12 = Student("Gaber", "Yasser", 1995, "male")
student_13 = Student("Rabab", "Sayed", 1985, "female")
student_14 = Student("Soliman", "Zakaria", 2004, "male")
#######################################################################################
# courses
#######################################################################################
course_01 = Course("Python Level 1", "Learn Python Level 1", 72)
course_02 = Course("Python Level 2", "Learn Python Level 2", 72)
course_03 = Course("HTML Level 1", "Learn HTML Level 1", 36)
course_04 = Course("HTML Level 2", "Learn HTML Level 2", 36)
course_05 = Course("CSS Level 1", "Learn CSS Level 1", 48)
course_06 = Course("CSS Level 2", "Learn CSS Level 2", 48)
course_07 = Course("Javascript Level 1", "Learn Javascript Level 1", 60)
course_08 = Course("Javascript Level 2", "Learn Javascript Level 2", 60)
course_09 = Course("FastAPI Level 1", "Learn FastAPI Level 1", 36)
course_10 = Course("FastAPI Level 2", "Learn FastAPI Level 2", 36)
#######################################################################################
# assign instructors to courses
#######################################################################################
course_01.assign_instructor(instructor_01)
course_02.assign_instructor(instructor_02)
course_03.assign_instructor(instructor_03)
course_04.assign_instructor(instructor_04)
course_05.assign_instructor(instructor_05)
#######################################################################################
# enroll students to courses
#######################################################################################
course_01.enroll_students(
    student_01,
    student_02,
    student_03,
    student_04,
    student_05,
    student_06,
    student_07
)
course_02.enroll_students(
    student_08,
    student_09,
    student_10,
    student_11,
    student_12,
    student_13,
    student_14
)
#######################################################################################
# assign a score to a student in a course
#######################################################################################
course_01.assign_score(student_01, 88)
course_01.assign_score(student_02, 44)
course_01.assign_score(student_03, 75)
course_01.assign_score(student_04, 92)
course_01.assign_score(student_05, 65)
course_01.assign_score(student_06, 71)
course_01.assign_score(student_07, 37)
#######################################################################################
# mark a student as completed a course
#######################################################################################
course_01.mark_completed(student_01)
course_01.mark_completed(student_03)
course_01.mark_completed(student_04)
course_01.mark_completed(student_05)
course_01.mark_completed(student_06)
#######################################################################################
# print course details
#######################################################################################
print(course_01)
print(course_02)
print(course_10)
#######################################################################################
# calculate the average scores of enrolled students in a course
#######################################################################################
print("Average score of course_01 is: ", course_01.average_score())
print("Average score of course_02 is: ", course_02.average_score())
#######################################################################################
# course management program ended
#######################################################################################
print("##########################################")
print("course management program ended")
print("##########################################")
#######################################################################################
