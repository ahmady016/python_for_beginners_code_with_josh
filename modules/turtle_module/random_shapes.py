# build a random shapes program using draw_shapes module as:
# ask the user to enter the number of shapes
# and randomly choose shapes from [circle, triangle, square, pentagon, hexagon]
# and randomly generate the sides, size, radius, color, thickness and position
# and loop to call draw_shapes or draw_circle to draw the shapes
##############################################################################
from turtle import done
from random import choice, randint
from draw_shapes import draw_circle, draw_star, draw_rectangle, draw_shape
##############################################################################
SHAPES = ["circle", "triangle", "star", "square", "rectangle", "pentagon", "hexagon", "heptagon", "octagon"]
SIDES = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8}
##############################################################################
def generate_random_color():
    # Generate a random integer between 0 and 0xFFFFFF (16777215) and Format it as a 6-digit hex string with a leading '#'
    return f"#{randint(0, 0xFFFFFF):06x}"
##############################################################################
print("#########################")
print("Random Shapes Program Completed Successfully")
print("#########################")
##############################################################################
# ask the user to enter the number of shapes
try:
    num_shapes = int(input("Enter the number of shapes: "))
    print("----------------------------")
except ValueError as error:
    print(error)
    print("you must enter a valid number")
    exit()
##############################################################################
# and randomly choose shapes from [circle, triangle, square, pentagon, hexagon]
# and randomly generate the sides, size, radius, color, thickness and position
for i in range(num_shapes):
    color = generate_random_color()
    thickness = randint(1, 10)
    position = (randint(-300, 300), randint(-200, 200))
    shape = choice(SHAPES)
    if shape == "circle":
        radius = randint(10, 100)
        draw_circle(radius=radius, color=color, thickness=thickness, position=position)
    elif shape == "star":
        width = randint(1, 10)
        size = randint(25, 125)
        draw_star(width=width, color=color, size=size, thickness=thickness, position=position)
    elif shape == "rectangle":
        width = randint(25, 125)
        height = randint(25, 125)
        draw_rectangle(width=width, height=height, color=color, thickness=thickness, position=position)
    else:
        sides = SIDES[shape]
        size = randint(25, 125)
        draw_shape(sides=sides, size=size, color=color, thickness=thickness, position=position)
    shape_num = i + 1
    shape_num = f"#{"0" + str(shape_num) if shape_num < 10 else shape_num}"
    print(f"shape_{shape_num} - ({shape}) \t with ({color}) color - was drawn successfully ...")
done()
##############################################################################
print("#########################")
print("Random Shapes Program Completed Successfully")
print("#########################")
##############################################################################
