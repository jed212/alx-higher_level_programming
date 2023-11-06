#!/usr/bin/python3
"""
Contains the MyList class that inherits from List
"""


class MyList(list):
    """A subclass of List"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted List"""
        print(sorted(self))
