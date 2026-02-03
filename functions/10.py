# create a students total score and grades calculator program using functions and dictionaries program as:
# -------------------------------------
# write a function that collect students names and scores as:
# collect the student's name and score in each subject
# subjects list:[math, science, english, history, geography] and each subject has a score between 0 and 100
# and store these values in a dictionary like:
# { "student name": { "math": 70, "science": 80, "english": 90, "history": 60, "geography": 50 } } }
# -------------------------------------
# then write a function that calculate the student's total score and grade as:
# total score = math + science + english + history + geography
# if the total score is equal to or more than 450 print "Excellent"
# if the total score is equal to or more than 400 print "Very Good"
# if the total score is equal to or more than 300 print "Good"
# if the total score is equal to or more than 200 print "Acceptable"
# if the total score is less than 200 print "Fail"
# and store each student's total score and grade in a dictionary like:
# { "student name": { "total_score": 450, "grade": "Excellent" } }
# -------------------------------------
# in the program ask the user to enter users names and scores and loop till the user enter 0
# finally in the program ask the user to enter a student name and print his total score and grade
# if the user enter a wrong name print "student not found"
# -------------------------------------
######################################################################
MIN_SCORE = 0
MAX_SCORE = 100
SUBJECTS = ["Mathematics", "Science", "English", "History", "Geography"]
STUDENTS_SCORES = {}
STUDENTS_GRADES = {}
######################################################################
def calculate_total_score(student_name):
    total_score = 0.0
    for score in STUDENTS_SCORES[student_name].values():
        total_score += score
    return total_score
######################################################################
def calculate_grade(total_score):
    if total_score >= 450:
        return "Excellent"
    elif total_score >= 400:
        return "Very Good"
    elif total_score >= 300:
        return "Good"
    elif total_score >= 200:
        return "Acceptable"
    else:
        return "Fail"
######################################################################
def calculate_student_grades(student_name):
        total_score = calculate_total_score(student_name)
        grade = calculate_grade(total_score)
        STUDENTS_GRADES[student_name] = { "total_score": total_score, "grade": grade }
######################################################################
def input_student_scores(student_name):
    student_scores = {}
    for subject in SUBJECTS:
        try:
            score = float(input(f"Enter {subject} score: "))
            if MIN_SCORE <= score <= MAX_SCORE:
                student_scores[subject] = score
            else:
                print("Subject score must be between 0 and 100")
                student_scores[subject] = 0
        except ValueError as error:
            print(error)
            print("Subject score must be a number")
    STUDENTS_SCORES[student_name] = student_scores
######################################################################
def print_students_scores():
    for name, scores in STUDENTS_SCORES.items():
        print(f"{name} scores are: {scores}")
######################################################################
def print_students_grades():
    for name, grade in STUDENTS_GRADES.items():
        print(f"{name} grade are: {grade}")
######################################################################
print("############################")
print("students total score and grades calculator program")
print("############################")
######################################################################
student_name = input("Enter student name or 0 to quit: ").upper()
print("----------------------------")
while student_name != "0":
    input_student_scores(student_name)
    calculate_student_grades(student_name)
    print("----------------------------")
    student_name = input("Enter student name or 0 to quit: ").upper()
    print("----------------------------")
######################################################################
if len(STUDENTS_SCORES) > 0:

    print_students_scores()
    print("----------------------------")

    print_students_grades()
    print("----------------------------")

    student_name = input("Enter student name to get its total score and grade: ").upper()
    print("----------------------------")

    if student_name in STUDENTS_GRADES.keys():
        total_score, grade = STUDENTS_GRADES[student_name].values()
        print(f"{student_name} total score is: {total_score} and grade is: {grade}")
    else:
        print("Student Not Found")

else:
    print("There are no students to get their total score and grade")
######################################################################
print("############################")
print("students total score and grades calculator program completed successfully")
print("############################")
######################################################################
