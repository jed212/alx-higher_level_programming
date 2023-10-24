#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        """
        instantiates class with a private instance attribut __size and an optional attribute 'size'
        checks if size is of type int else, raises a TypeError,
        checks if size < 0 and raises a VauleError
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

