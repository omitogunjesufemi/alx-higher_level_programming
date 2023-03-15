#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        n_list = []
        for j in row:
            n_list.append(j ** 2)
        new_matrix.append(n_list)
    return new_matrix
