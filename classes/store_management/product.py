########################################################################################
from helpers import generate_id
########################################################################################
class Product:
    def __init__(self, name, description, category):
        self.id = generate_id(8)
        self.name = name
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.category} - {self.description}"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.name == other.name and self.category == other.category

