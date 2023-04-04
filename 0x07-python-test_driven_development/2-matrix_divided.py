#!/usr/bin/python3

"""This module divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """Divdes all element of a matrix"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    size = 0
    counter = 0
    for items in matrix:

        if type(items) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if counter > 0:
            if len(matrix[counter - 1]) != len(matrix[counter]):
                raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for element in items:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            element = round(float(element) / div, 2)
            new_list.append(element)
        new_matrix.append(new_list)
        counter += 1
    return new_matrix
