#!/usr/bin/python3
"""This module contains a function that returns an object (Python data
structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """A function that returns the object (Python Data Structure)
    represented by a JSON string
    """
    py_obj = json.loads(my_str)
    return py_obj
