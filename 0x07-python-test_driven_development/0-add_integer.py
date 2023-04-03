#!/usr/bin/python3
"""This module adds two integers together

    Returns: a + b

    TypeError: a must be an integer or b must be an integer

"""
def add_integer(a, b=98):
    """ Adds 2 integers

    Returns: a + b

    TypeError: a must be an integer or b must be an integer
    """
    if type(a) in [int, float]:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) in [int, float]:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
