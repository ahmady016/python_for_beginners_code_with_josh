# build a shapes drawer program using the draw_shapes module as:
# ask the user to enter which shape he wants to draw [triangle, square, pentagon, hexagon]
# if the user enter triangle then draw a triangle and ask for the size, color, thickness and position
# if the user enter square then draw a square and ask for the size, color, thickness and position
# if the user enter pentagon then draw a pentagon and ask for the size, color, thickness and position
# if the user enter hexagon then draw a hexagon and ask for the size, color, thickness and position
# otherwise print an error message
###################################################################
from turtle import exitonclick
from draw_shapes import draw_triangle, draw_square, draw_pentagon, draw_hexagon
###################################################################
print("##########################")
print("Shapes Drawer Program")
print("##########################")
###################################################################
user_name = input("Enter your name: ").upper()
start = input("Do you want to draw a shape? [y/n]: ")
print("-------------------------")
###################################################################
while start == "y":
    shape = input("Enter which shape you want to draw (triangle, square, pentagon, hexagon): ").lower()
    match shape:
        case "triangle":
            draw_triangle()
        case "square":
            draw_square()
        case "pentagon":
            draw_pentagon()
        case "hexagon":
            draw_hexagon()
        case _:
            print(f"Opps, {user_name}, this shape is not available")
            print("-------------------------")
    exitonclick()
    start = input("Do you want to draw another shape? [y/n]: ")
###################################################################
print("Shapes Drawer Program Completed Successfully")
print("-------------------------")
###################################################################
