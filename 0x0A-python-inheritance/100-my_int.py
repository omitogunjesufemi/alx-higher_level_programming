#!/usr/bin/python3
"""This module creates a MyInt class that inherits from int
It contains magic methods implemented with it
__eq__, and __ne__
"""


class MyInt(int):
    """MyInt class that inherits from int
    It contains magic methods implemented with it
    __eq__, and __ne__
    """
    def __new__(self, value):
        """Creates a new instance
        """
        return super().__new__(self, value)

    def __init__(self, value):
        """Initialises the class
        """
        self.value = value

    def __eq__(self, other):
        """Magic methods for ==
        """
        return (self.value != other)

    def __ne__(self, other):
        """Magic methods for !=
        """
        return (self.value == other)
