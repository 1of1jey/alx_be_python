import math

class Shape:

    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

    class Rectangle(Shape):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
                return self.length * self.width