# build a program that benefit from sets
# the program should collect the user's name
# given a courses list like:
# ["MS Office", "2D Graphics", "Frontend Web"]
# and a list of trainees names like:
# ["Tamer Hessen", "Ahmed Belal", "Osman Ali", "Ahmed Ali", "Eman Nasr", "Yasser Zeddan", "Ali Nasr"]
# create a set for each course containing the trainees names by
# using the random module to randomly pick a trainees to each course
# then print the trainees names in each course
# and print all the trainees names from all courses
# and print the trainees names that are enrolled in all the courses
# and print the trainees names that are enrolled only in one course
# and print the trainees names that are enrolled only in both the MS Office and 2D Graphics
######################################################################
from random import choice
######################################################################
print("############################")
print("trainees courses analyzer program")
print("############################")
######################################################################
courses = ["MS Office", "2D Graphics", "Frontend Web"]
trainees = ["Tamer Hessen", "Ahmed Belal", "Osman Ali", "Ahmed Ali", "Eman Nasr", "Yasser Zeddan", "Ali Nasr", "Mohammed Ali", "Omar Salah", "Mohammed Salah", "Yasser Adel"]
######################################################################
ms_office = {"Osama Osman"}
two_d_graphics = {"Shrifa Arafat"}
frontend_web = {"Sayed Osman"}
######################################################################
for i in range(8):
    ms_office.add(choice(trainees))
    two_d_graphics.add(choice(trainees))
    frontend_web.add(choice(trainees))
######################################################################
print("all trainees names:")
print(ms_office | two_d_graphics | frontend_web)
######################################################################
print("trainees names enrolled in all courses:")
print(ms_office & two_d_graphics & frontend_web)
######################################################################
print("trainees names enrolled only in MS Office or only in 2D Graphics but not both:")
print(ms_office ^ two_d_graphics)
######################################################################
print("trainees names enrolled only in both MS Office and 2D Graphics:")
print(ms_office & two_d_graphics)
######################################################################
print("trainees names enrolled only in MS Office:")
print(ms_office - (two_d_graphics | frontend_web))
######################################################################
print("trainees names enrolled only in 2D Graphics:")
print(two_d_graphics - (ms_office | frontend_web))
######################################################################
print("trainees names enrolled only in Frontend Web:")
print(frontend_web - (ms_office | two_d_graphics))
######################################################################
print("trainees names enrolled in MS Office:")
print(ms_office)
######################################################################
print("trainees names enrolled in 2D Graphics:")
print(two_d_graphics)
######################################################################
print("trainees names enrolled in Frontend Web:")
print(frontend_web)
######################################################################
print("############################")
print("trainees courses analyzer program completed successfully")
print("############################")
######################################################################
