# build a simple math multiplication table program using a for loop as:
# collect the number of rows and columns
# loop in every row and column
# and print the multiplication table
#######################################################################
print("##################################")
print("Simple Math Multiplication Table")
print("##################################")
#########################################################################
try:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
except ValueError as error:
    print(error)
    print("you must enter a valid number")
except Exception as error:
    print(error)
    print("something went wrong")
finally:
    print("----------------------------------")
#########################################################################
for row in range(1, rows + 1):
    for column in range(1, columns + 1):
        print(f"{row} x {column} = {row * column}")
    print("----------------------------------")
#########################################################################
print("##################################")
print("Simple Math Multiplication Table Completed Successfully")
print("##################################")
#########################################################################
