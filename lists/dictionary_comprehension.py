##################################################################
# build an employees salaries analyzer program using dictionary comprehension:
# given a dictionary of employees and their annual salaries like:
# {"Ahmed": 34000, "Mohamed": 30000, "Ali": 32000, "Osama": 40000, "Sayed": 50000, "Eman": 45000, "Osman": 66000}
# print each employee name and salary like: "Ahmed earned $34000 in a year"
# and get only employees that earn more than 50000
# and get only employees that earn less than 30000
# and get only employees that earn between 30000 and 50000
##################################################################
employees = {
    "Ahmed": 66000,
    "Mohamed": 30000,
    "Ali": 27000,
    "Osama": 40000,
    "Sayed": 50000,
    "Eman": 45000,
    "Fawzy": 36000,
    "Omar": 44000,
    "Yasser": 24000,
    "Zeddan": 40000,
    "Osman": 57000,
    "Shrifa": 47000
}
##################################################################
print("################################")
print("employees salaries analyzer program")
print("################################")
##################################################################
print("employees info:")
print("------------------------------------")
employees_info = [f"{name} earned ${salary} in a year" for name, salary in employees.items()]
for employee in employees_info:
    print(employee)
print("------------------------------------")
##################################################################
higher_than_50000 = {name: salary for name, salary in employees.items() if salary > 50000}
print(f"#{len(higher_than_50000)} employees that earn more than 50000:")
print("------------------------------------")
print(higher_than_50000)
print("------------------------------------")
##################################################################
lower_than_40000 = {name: salary for name, salary in employees.items() if salary < 40000}
print(f"#{len(lower_than_40000)} employees that earn less than 40000:")
print("------------------------------------")
print(lower_than_40000)
print("------------------------------------")
##################################################################
between_40000_and_50000 = {name: salary for name, salary in employees.items() if salary >= 40000 and salary <= 50000}
print(f"#{len(between_40000_and_50000)} employees that earn between 40000 and 50000:")
print("------------------------------------")
print(between_40000_and_50000)
print("------------------------------------")
##################################################################
