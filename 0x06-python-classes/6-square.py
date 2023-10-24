#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate with optional attributes size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """To retrieve a private instance attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set a private instance attribute"""
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """retrieve private instance attribute position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """To set a private instance attribute position"""
        self.__position = value
        
        if not isinstance((value, value),(int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates area and returns it"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
