#!/usr/bin/python3
"""Defines a function that appends to a file."""


def append_write(filename="", text=""):
    """
    A function that appends a string to the end of a UTF8 text file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
