#!/usr/bin/python3
"""Create class Rectangle"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Instantiate with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        To retrieve the private intance attribute width
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
