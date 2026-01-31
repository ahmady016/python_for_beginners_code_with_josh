# build an employees salaries analyzer program:
# given a list of employees and their annual salaries
# like: ["Ahmed_34000", "Mohamed_30000", "Ali_32000"]
# you need to loop throw the list and get each employee salary
# and calculate and print the grand total of salaries and average salary
################################################
print("####################")
print("employees salaries analyzer program")
print("####################")
################################################
employees = ["Ahmed_34000", "Mohamed_30000", "Ali_32000", "Osama_40000", "Sayed_50000", "Eman_45000", "Osman_66000"]
total = 0
for employee in employees:
    employee_salary = int(employee.split("_")[1])
    total += employee_salary
average_salary = round(total / len(employees), 2)
################################################
print("grand total of salaries:", total)
print("average salary:", average_salary)
################################################
