#######################################################################################
from shape import Shape
#######################################################################################
class Heptagon(Shape):
    AREA_COEFFICIENT = 3.6339
    def __init__(self, size, color, thickness=1, position=(0, 0)):
        super().__init__("heptagon", 7, size, color, thickness, position)

    def calculate_area(self):
        return Heptagon.AREA_COEFFICIENT * (self.size ** 2)

    def calculate_perimeter(self):
        return self.size * 7
