#######################################################################################
import math
from shape import Shape
#######################################################################################
class Circle(Shape):
    def __init__(self, radius, color, thickness=1, position=(0, 0)):
        super().__init__("Circle", sides=0, size=radius, color=color, thickness=thickness, position=position)
        self.radius = radius

    def draw(self):
        # up the pen and move to the position and down the pen again to draw
        self.turtle.penup()
        self.turtle.goto(self.position)
        self.turtle.pendown()
        # draw the circle and fill it
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.size

    def __str__(self):
        return f"{self.name}(radius={self.radius}, color={self.color}, thickness={self.thickness}, position={self.position})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius
