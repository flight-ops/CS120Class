import math
#create a hierarchy of shapes
#include a base class, "Shape"
#then make two derived classes, Circle and Rectangle

class Shape():
    def __init__(self,shape_area, shape_perimeter) -> None:
        self.area = float(shape_area)
        self.perimeter = float(shape_perimeter)

    def find_area(self):
        print(self.area)

    def find_perimeter(self):
        print(self.perimeter)



class Circle(Shape):
    def __init__(self, radius) -> None:
        self.area = float(math.pi*(radius**2))
        self.perimeter = float(2*math.pi*radius)
        
class Rectangle(Shape):
     def __init__(self, width, height) -> None:
        self.area = (width * height)
        self.perimeter = (2*width + 2*height)

        

example_circle = Circle(radius=10)

example_circle.find_area()

example_rectangle = Rectangle(width=4,height=10)

example_rectangle.find_area()