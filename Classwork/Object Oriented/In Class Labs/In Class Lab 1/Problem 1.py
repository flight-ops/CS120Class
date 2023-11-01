#create a hierarchy of shapes
#include a base class, "Shape"
#then make two derived classes, Circle and Rectangle

class Shape():
    def __init__(self,shape_area, shape_perimeter) -> None:
        self.area = shape_area
        self.perimeter = shape_perimeter

    def find_area(self):
        print(self.area)

    def find_perimeter(self):
        print(self.perimeter)


base_shape = Shape(shape_area=200,shape_perimeter=20)

base_shape.find_area
