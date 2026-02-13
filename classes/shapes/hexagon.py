#######################################################################################
from shape import Shape
#######################################################################################
class Hexagon(Shape):
    AREA_COEFFICIENT = 2.598
    def __init__(self, size, color, thickness=1, position=(0, 0)):
        super().__init__("Hexagon", 6, size, color, thickness, position)

    def calculate_area(self):
        return  Hexagon.AREA_COEFFICIENT * (self.size ** 2)

    def calculate_perimeter(self):
        return self.size * 6
