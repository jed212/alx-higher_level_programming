#!/usr/bin/python3
""" Create a class Rectangle"""


class Rectangle:
    """
    Represents a Rectangle
    number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiate with optional width and height
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        To retrieve the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        To set the private instance attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        To retrieve the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        To set the private instance attribute height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns Rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Takes two rectangles (rect_1 and rect_2)as arguments and
        Returns the rectangle with the greater area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Prints the rectangle with character '#' """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [
                    rectangle.append(str(self.print_symbol))
                    for j in range(self.__width)
            ]
            if i != self.__height - 1:
                rectangle.append('\n')
        return ("".join(rectangle))

    def __repr__(self):
        """ Returns the string representation of the rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """ Prints a message for every deletion of a Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
