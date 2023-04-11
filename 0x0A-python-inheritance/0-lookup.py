#!/usr/bin/python3
"""This modules contains a function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """lookup: A function that returns the list of available
    attributes and methods of an object

    Return:
        list object
    """
    return dir(obj)
