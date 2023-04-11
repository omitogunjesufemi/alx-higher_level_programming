#!/usr/bin/python3
"""1-mylist module creates a class MyList which injerits from list.
It contains a class which contains a public instance method
"""


class MyList(list):
    """MyList inherits from list

    Public Instance Method:
        print_sorted(self)

    It is assumed that all the elements of the list will be
    of the type int
    """
    def print_sorted(self):
        """It prints the list but sorted in ascending order

        All the elements of the list are of type int
        """
        new_list = self[:]
        print(sorted(new_list))
