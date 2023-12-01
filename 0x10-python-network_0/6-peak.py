#!/usr/bin/python3
"""This module contains a function that finds a peak in a list of
unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers """
    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    low = 1
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return (list_of_integers[mid])

        if list_of_integers[mid] >= list_of_integers[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1
    return (None)
