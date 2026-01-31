#######################################################################
# build a list of numbers from 1 to 20 using a list comprehension
# and print the list
# and print the sum of the list
# and print the average of the list
# and print the odd numbers in the list
# and print the even numbers in the list
# and print the length of the odd numbers in the list
# and print the length of the even numbers in the list
# and print the sum of the odd numbers in the list
# and print the sum of the even numbers in the list
# and print the average of the odd numbers in the list
# and print the average of the even numbers in the list
# finally print the square numbers in the list
#######################################################################
print("####################")
print("list comprehension")
print("####################")
#######################################################################
numbers = [number for number in range(1, 21)]
square_numbers = [number ** 2 for number in numbers]
odd_numbers = [number for number in numbers if number % 2 == 1]
even_numbers = [number for number in numbers if number % 2 == 0]
######################################################################
print("numbers list:", numbers)
print("sum of numbers:", sum(numbers))
print("average of numbers:", sum(numbers) / len(numbers))
######################################################################
print("odd numbers:", odd_numbers)
print("length of odd numbers:", len(odd_numbers))
print("sum of odd numbers:", sum([number for number in numbers if number % 2 == 1]))
print("average of odd numbers:", sum([number for number in numbers if number % 2 == 1]) / len([number for number in numbers if number % 2 == 1]))
######################################################################
print("even numbers:", even_numbers)
print("length of even numbers:", len(even_numbers))
print("sum of even numbers:", sum([number for number in numbers if number % 2 == 0]))
print("average of even numbers:", sum([number for number in numbers if number % 2 == 0]) / len([number for number in numbers if number % 2 == 0]))
######################################################################
print("square numbers:", square_numbers)
######################################################################
print("####################")
print("list comprehension completed successfully")
print("####################")
#######################################################################
