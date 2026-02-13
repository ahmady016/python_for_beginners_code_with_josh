######################################################################################
from turtle import Turtle
######################################################################################
class Shape:
    def __init__(self, name, sides, size, color, thickness=1, position=(0, 0)):
        self.name = name
        self.sides = sides

        self.size = size
        self.color = color
        self.thickness = thickness
        self.position = position

        self.turtle = Turtle()
        self.turtle.color(self.color)
        self.turtle.pensize(self.thickness)

    def draw(self):
        # up the pen and move to the position and down the pen again to draw
        self.turtle.penup()
        self.turtle.goto(self.position)
        self.turtle.pendown()
        # draw the regular shape using each side and fill it
        self.turtle.begin_fill()
        for i in range(self.sides):
            self.turtle.forward(self.size)
            self.turtle.left(360 / self.sides)
        self.turtle.end_fill()

    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

    def __str__(self):
        return f"{self.name}(sides={self.sides}, size={self.size}, color={self.color}, thickness={self.thickness}, position={self.position})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.name == other.name and self.sides == other.sides
######################################################################################
