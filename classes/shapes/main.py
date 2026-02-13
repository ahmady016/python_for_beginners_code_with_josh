# build a shapes using oop and inheritance to handle various shapes:
# ------------------------------------------------------------------
# create a base shape class that contains
# the sides, size, color, thickness and position
# for each shape create a shape classes that inherits from the base shape
# and each one assigns a specific number of sides, size, color, thickness and position
# example of regular sides shapes: triangle, square, pentagon, hexagon, heptagon, octagon
# example of irregular sides shapes: rectangle, circle
# use the math module to calculate the area and perimeter of the shapes
# use the turtle module to draw the shapes
#########################################################################################
# finally test all the shapes with different sizes, colors and positions
# by creating each shape object and give it an example size, color and position
# and calculate the area and perimeter of the shapes
# you can use random modules for random sizes, colors and positions
#########################################################################################
from random import randint, choice
from turtle import done

from triangle import Triangle
from square import Square
from pentagon import Pentagon
from hexagon import Hexagon
from heptagon import Heptagon
from octagon import Octagon
from circle import Circle
from rectangle import Rectangle
#########################################################################################
COLORS = ["black", "red", "green", "blue", "yellow", "black", "orange", "purple", "pink", "brown", "gray", "navy", "teal", "maroon", "olive", "violet", "cyan"]
REGULAR_SHAPES = [Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon]
#########################################################################################
print("########################################")
print("Drawing Shapes with OOP and Inheritance Started")
print("########################################")
#########################################################################################
print("Test Regular Shapes:")
print("-------------------------")
for ShapeType in REGULAR_SHAPES:
    size = randint(50, 150)
    color = choice(COLORS)
    thickness = randint(1, 10)
    position = (randint(-300, 300), randint(-200, 200))
    shape = ShapeType(size, color, thickness, position)

    print(f"Drawing: {shape}")
    print("-------------------------")
    shape.draw()

    print(f"{shape.name} Area: {round(shape.calculate_area(), 2)}")
    print(f"{shape.name} Perimeter: {shape.calculate_perimeter()}")

    print("-------------------------")

print("Test Irregular Shapes:")
print("-------------------------")

print("Circle:")
print("-------------------------")
radius = randint(25, 100)
color = choice(COLORS)
position = (randint(-300, 300), randint(-200, 200))
thickness = randint(1, 10)
circle = Circle(radius, color, thickness, position)

print(f"Drawing: {circle}")
print("-------------------------")
circle.draw()

print(f"{circle.name} Area: {round(circle.calculate_area(), 2)}")
print(f"{circle.name} Perimeter: {circle.calculate_perimeter()}")
print("-------------------------")

print("Rectangle:")
print("-------------------------")
width = randint(50, 150)
height = randint(50, 150)
color = choice(COLORS)
thickness = randint(1, 10)
position = (randint(-300, 300), randint(-200, 200))
rectangle = Rectangle(width, height, color, thickness, position)

print(f"Drawing: {rectangle}")
print("-------------------------")
rectangle.draw()

print(f"{rectangle.name} Area: {round(rectangle.calculate_area(), 2)}")
print(f"{rectangle.name} Perimeter: {rectangle.calculate_perimeter()}")
print("-------------------------")
done()
#########################################################################################
print("########################################")
print("Drawing Shapes with OOP and Inheritance Finished")
print("########################################")
#########################################################################################
