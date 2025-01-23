import math


class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError("derived classes need to override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        area_Rectangle = self.length * self.width
        return area_Rectangle

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()
    
    def area(self):
        area_Circle = math.pi * self.radius ** 2
        return area_Circle

    
