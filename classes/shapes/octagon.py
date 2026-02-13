#######################################################################################
from shape import Shape
#######################################################################################
class Octagon(Shape):
    AREA_COEFFICIENT = 4.8284
    def __init__(self, size, color, thickness=1, position=(0, 0)):
        super().__init__("octagon", 8, size, color, thickness, position)

    def calculate_area(self):
        return Octagon.AREA_COEFFICIENT * (self.size ** 2)

    def calculate_perimeter(self):
        return self.size * 8
