#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        """instantiates a private instance attribute"""
        self.__size = size

    @property
    def size(self):
        """to retrieve the private instance attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """to set a private instance attribute"""
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """to calculate the area and return it"""
        return (self.__size ** 2)



