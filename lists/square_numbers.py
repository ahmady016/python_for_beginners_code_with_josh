# build a square numbers program as:
# collect the user name and a list of numbers input separated by comma
# and convert them to integers and store then in a numbers_list
# and create a new square_numbers_list using list comprehension
# finally print the numbers_list and the square_numbers_list
######################################################################
print("####################")
print("square numbers program")
print("####################")
######################################################################
user_name = input("Enter your name: ").upper()
print("----------------------------")
numbers_string = input("Enter numbers separated by comma: ").split(", ")
print("----------------------------")
######################################################################
numbers_list = [int(number) for number in numbers_string]
square_numbers_list = [number ** 2 for number in numbers_list]
######################################################################
print(f"Hi {user_name}, your entered #{len(numbers_list)} numbers and these are your numbers:")
print("----------------------------")
print(f"{numbers_list}")
print("----------------------------")
print(f"and your square numbers:")
print("----------------------------")
print(f"{square_numbers_list}")
print("----------------------------")
######################################################################
print("####################")
print("square numbers program completed successfully")
print("####################")
######################################################################
