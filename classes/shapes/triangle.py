########################################################################################
import math
from shape import Shape
########################################################################################
class Triangle(Shape):
    AREA_COEFFICIENT = 0.433
    def __init__(self, size, color, thickness=1, position=(0, 0)):
        super().__init__("Triangle", 3, size, color, thickness, position)

    def calculate_area(self):
        return Triangle.AREA_COEFFICIENT * (self.size ** 2)

    def calculate_perimeter(self):
        return self.size * 3
