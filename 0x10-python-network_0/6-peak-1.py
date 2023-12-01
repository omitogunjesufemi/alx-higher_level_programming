#!/usr/bin/python3
"""This module contains a function that finds a peak in a list of
unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers """
    if list_of_integers is None:
        return None

    i = 0
    while (i < len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] >= list_of_integers[i + 1]:
                return (list_of_integers[i])

        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] >= list_of_integers[i - 1]:
                return (list_of_integers[i])

        else:
            if list_of_integers[i - 1] < list_of_integers[i] \
               and list_of_integers[i] > list_of_integers[i + 1]:
                return (list_of_integers[i])

        i = i + 1
