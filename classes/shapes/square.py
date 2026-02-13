###############################################################################
from shape import Shape
###############################################################################
class Square(Shape):
    def __init__(self, size, color, thickness=1, position=(0, 0)):
        super().__init__("Square", 4, size, color, thickness, position)

    def calculate_area(self):
        return self.size ** 2

    def calculate_perimeter(self):
        return self.size * 4
