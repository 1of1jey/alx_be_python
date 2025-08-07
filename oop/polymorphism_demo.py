import math

class Shape:

    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

    class Rectangle(Shape):
        """Rectangle class that inherits from Shape."""

        def __init__(self, length, width):
            self.length = length
            self.width = width