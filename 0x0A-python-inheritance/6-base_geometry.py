#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent a base geometry."""

    def area(self):
        """Raises a not implemented error."""
        raise Exception("area() is not implemented")
