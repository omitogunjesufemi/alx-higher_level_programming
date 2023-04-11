#!/usr/bin/python3
"""This module contains a function that adds a new attribute to
an object if it’s possible
"""


def add_attribute(class_name, attribute_name, attribute_value):
    """A function that adds a new attribute to an object if it’s
    possible:

    Raise a TypeError exception, with the message can't add new
    attribute if the object can’t have new attribute
    """
    if type(class_name) in [list, int, bool, float, str,
                            dict, tuple, range, complex, set,
                            bytearray, bytes, memoryview]:
        raise TypeError("can't add new attribute")
    setattr(class_name, attribute_name, attribute_value)
    if hasattr(class_name, attribute_name) is not True:
        raise TypeError("can't add new attribute")
