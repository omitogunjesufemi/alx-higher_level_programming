"""This module contains a function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers representing the
    Pascal's triangle of n:

    Returns an empty list if n <= 0

    where n will be always an integer
    """

    list_t = []
    if n <= 0:
        return list_t

    for i in range(n):
        if i == 0:
            list_t.append([1])
        else:
            sub_list = [0]+list_t[i - 1]+[0]
            new_sub_list = []
            for x in range(len(sub_list) - 1):
                new_sub_list.append(sub_list[x] + sub_list[x + 1])
            list_t.append(new_sub_list)

    return list_t
