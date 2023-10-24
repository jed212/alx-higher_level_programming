#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Define a class Square."""

    def __init__(self, size=0):
        """instantiates a private instance attribute 'size' and an optional attribute 'size'"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates and returns the current square area"""
        return (self.__size ** 2)
