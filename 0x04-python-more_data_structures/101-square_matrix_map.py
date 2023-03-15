#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda x: x**2, [row[i] for row in matrix
                     for i in range(len(matrix))])))
