#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)

    if matrix_len > 0:
        for row in matrix:
            row_len = len(row)
            i = 0
            for item in row:
                if i < row_len - 1:
                    print('{:d}'.format(item), end=" ")
                else:
                    print('{:d}'.format(item), end="\n")
                i += 1

    else:
        print()
