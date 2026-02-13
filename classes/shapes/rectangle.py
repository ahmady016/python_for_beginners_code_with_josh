#######################################################################################
from shape import Shape
#######################################################################################
class Rectangle(Shape):
    def __init__(self, width, height, color, thickness=1, position=(0, 0)):
        super().__init__("Rectangle", 4, (width + height) / 2, color, thickness, position)
        self.width = width
        self.height = height

    def draw(self):
        # up the pen and move to the position and down the pen again to draw
        self.turtle.penup()
        self.turtle.goto(self.position)
        self.turtle.pendown()
        # draw the rectangle and fill it
        self.turtle.begin_fill()
        for i in range(2):
            self.turtle.forward(self.width)
            self.turtle.left(90)
            self.turtle.forward(self.height)
            self.turtle.left(90)
        self.turtle.end_fill()

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return f"{self.name}(width={self.width}, height={self.height}, color={self.color}, thickness={self.thickness}, position={self.position})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height
