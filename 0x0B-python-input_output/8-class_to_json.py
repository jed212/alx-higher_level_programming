#!/usr/bin/python3
"""Defines a function that converts a Python class to JSON."""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure."""
    return obj.__dict__
