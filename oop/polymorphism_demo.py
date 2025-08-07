import math

class Shape:

    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

    class Rectangle(Shape):
        """Rectangle class that inherits from Shape."""

        def __init__(self, length, width):
            """Initialize a Rectangle with length and width.

            Args:
                length (float): The length of the rectangle.
                width (float): The width of the rectangle.
            """
            self.length = length
            self.width = width