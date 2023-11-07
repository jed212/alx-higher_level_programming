#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function that converts an object to JSON."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string."""
    return json.loads(my_str)
