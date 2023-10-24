#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        """instantiates with optional attribute 'size'"""
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
        """calculates current square area and returns it"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with thhe character #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
