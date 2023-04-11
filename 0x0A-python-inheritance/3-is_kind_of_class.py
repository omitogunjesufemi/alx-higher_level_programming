#!/usr/bin/python3
"""This module returns True if the object is an instance of the parent
class or an instance of the derived class
"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an instance of, or
    if the object is an instance of a class that inherited from, the
    specified class ; otherwise False.
    """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
