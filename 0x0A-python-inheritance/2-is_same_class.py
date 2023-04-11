#!/usr/bin/python3
"""The module contains a function is_same_class which returns True
if the object is exactly an instance of the specified class;
otherwise False
"""


def is_same_class(obj, a_class):
    """is_same_class returns True if the object is exactly an instance
    of the specified class otherwise False

    Arguments:
        obj: list object
        a_class: class to compare with
    """
    if isinstance(obj, a_class) and a_class is not object:
        return True
    else:
        return False
