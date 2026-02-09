# build a basic HR system for a company that divides employees data into:
# personal, qualification, contact and job information
# using multiple classes with multiple inheritance
#######################################################################################
from employee import Employee
#######################################################################################
print("####################")
print("employees HR system")
print("####################")
#######################################################################################
ahmed = Employee("Ahmed", "Osman", 1995, "Male", "Cairo", "0123456789", "H4gZK@example.com", "Bachelor", 2016, 85, "2017-01-01", "IT Helpdesk", "IT", 8000)
omar = Employee("Omar", "Salah", 1992, "Male", "Cairo", "0123456789", "H4gZK@example.com", "Bachelor", 2014, 75, "2016-01-01", "Network Engineer", "IT", 11000)
yasser = Employee("Yasser", "Mohammed", 2001, "Male", "Cairo", "0123456789", "H4gZK@example.com", "Bachelor", 2022, 90, "2024-01-01", "Software Engineer", "IT", 14000)
#######################################################################################
print("employees info:")
print("------------------------------------")
print(ahmed)
print("------------------------------------")
print(omar)
print("------------------------------------")
print(yasser)
print("------------------------------------")
#######################################################################################
print("employees info:")
print("------------------------------------")
print(repr(ahmed))
print("------------------------------------")
print(repr(omar))
print("------------------------------------")
print(repr(yasser))
print("------------------------------------")
#######################################################################################
