########################################################################################
from shape import Shape
########################################################################################
class Pentagon(Shape):
    AREA_COEFFICIENT = 1.72048
    def __init__(self, size, color, thickness=1, position=(0, 0)):
        super().__init__("Pentagon", 5, size, color, thickness, position)

    def calculate_area(self):
        return Pentagon.AREA_COEFFICIENT * (self.size ** 2)

    def calculate_perimeter(self):
        return self.size * 5
