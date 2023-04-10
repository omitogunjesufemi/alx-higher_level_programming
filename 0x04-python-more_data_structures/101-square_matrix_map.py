#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return([(map(lambda x: x**2, [r[i] for r in matrix for i in range(len(matrix))]))])
