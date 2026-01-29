# create a function that accept student name and score and calculate the student's grade as
# if the score is equal to or more than 90 print A
# if the score is equal to or more than 80 print B
# if the score is equal to or more than 70 print C
# if the score is equal to or more than 60 print D
# if the score is less than 60 print F

def get_student_grade(name, score):
    if score >= 90:
        return f"{name} your grade is A"
    elif score >= 80:
        return f"{name} your grade is B"
    elif score >= 70:
        return f"{name} your grade is C"
    elif score >= 60:
        return f"{name} your grade is D"
    else:
        return f"{name} your grade is F"

print("student grade calculator program")
print("--------------------------------")
student_name = input("Enter your name: ").upper()
student_score = int(input("Enter your score: "))
print("--------------------------------")
student_grade = get_student_grade(student_name, student_score)
print(student_grade)
print("--------------------------------")
