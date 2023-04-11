#!/usr/bin/python3
"""This module returns True if the object is an instance of a class that
inherited directly or indirectly from the specified class; otherwise
False
"""


def inherits_from(obj, a_class):
    """A function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified
    class ; otherwise False.

    Args:
        obj
        a_class
    """
    if (issubclass(type(obj), a_class) and obj.__class__ is not a_class):
        return True
    else:
        return False
