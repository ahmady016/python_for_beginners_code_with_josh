# build a programming languages list program as:
# collect the user name
# and collect a list of programming languages from one input separated by space
# then store them in a list
# and print the first and last programming languages in the list
# and print the number of programming languages in the list
#################################################
print("####################")
print("programming languages list program")
print("####################")
#################################################
user_name = input("Enter your name: ").upper()
print("----------------------------")
programming_languages = input("Enter programming languages separated by space: ").split(" ")
print("----------------------------")
#################################################
print(f"Hi {user_name}, your entered #{len(programming_languages)} programming languages")
print(f"and your first programming language is {programming_languages[0]}")
print(f"and your last programming language is {programming_languages[-1]}")
#################################################
print("####################")
print("programming languages list program completed successfully")
print("####################")
#################################################
