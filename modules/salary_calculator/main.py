# build an Employees salary calculator program using helpers module as:
# there are two types of employees [full time, part time]
# for each type create function to calculate the salary

# the part time employee function accept the number of hours worked and the hourly rate
# then multiply the number of hours worked by the hourly rate

# the full time employee function accept experience years and base annual salary
# if the employee experience is over 10 years he get 3x raise and a bonus of $3000
# if the employee experience is between 5 and 10 years he get 2x raise and a bonus of $2000
# if the employee experience is between 2 and 4 years he get 1.5x raise and a bonus of $1000
# if the employee experience is less than 2 years he don't get a raise and get a bonus of $500

# in the main program create a loop to start or quit the program
# every time it runs, ask for employee's name and type [full-time, part-time]
# if the type is part-time ask for the number of hours worked and the hourly rate and call the part time employee function
# if the type is full-time ask for the experience years and base annual salary and call the full time employee function
# otherwise print "you are unemployed!"
# print the employee's name and salary for each one

from part_time import part_time_salary
from full_time import full_time_salary

print("employees salary calculator program")
print("---------------------------------")

start = int(input("Enter 1 to start and 0 to quit: "))
print("---------------------------------")
while start == 1:
    employee_name = input("Enter your name: ").upper()
    employee_type = input("Enter your type [full-time, part-time]: ").lower()
    print("---------------------------------")

    if employee_type == "part-time":
        hours_worked = float(input("Enter the number of hours worked: "))
        hourly_rate = float(input("Enter the hourly rate: "))
        print("---------------------------------")
        print(f"Hi {employee_name}, your salary is ${part_time_salary(hourly_rate, hours_worked)}")
        print("---------------------------------")
    elif employee_type == "full-time":
        years_of_experience = int(input("Enter the years of experience: "))
        base_annual_salary = float(input("Enter the base annual salary: "))
        print("---------------------------------")
        print(f"Hi {employee_name}, your salary is ${full_time_salary(base_annual_salary, years_of_experience)}")
        print("---------------------------------")
    else:
        print("you are unemployed!")
        print("---------------------------------")

    start = int(input("Enter 1 to start and 0 to quit: "))
    print("---------------------------------")

print("employees salary calculator program finished")
print("---------------------------------")
