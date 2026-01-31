# build a students class assigner program as:
# collect all the students names in one input separated by space and store them in a list
# then loop through the list and assign each student to a random class between 1 and 3
# at the end print each student name and there corresponding class
######################################################
from random import randint
######################################################
print("############################")
print("student class assigner program")
print("############################")
######################################################
students = input("Enter all the students names separated by space: ").split(" ")
print("========================")
classes = []
for student in students:
    classes.append(f"class#{randint(1, 3)}")
######################################################
print("Here are the students and their corresponding classes:")
print("========================")
students_count = len(students)
for i in range(students_count):
    print(f"Hi {students[i]}, you are in {classes[i]}")
######################################################
print("############################")
print("student class assigner program completed successfully")
print("############################")
######################################################
