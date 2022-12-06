#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    list_a = [x for x in tuple_a]
    list_b = [x for x in tuple_b]
    list_a = list_a[:2]
    list_b = list_b[:2]
    result_tuple = ()

    if len_a < 2:
        if len_a == 0:
            list_a[0:2] = [0, 0]
        elif len_a == 1:
            list_a[1] = 0
    if len_b < 2:
        if len_b == 0:
            list_b[0:2] = [0, 0]
        elif len_b == 1:
            list_b[1:2] = [0]

    result = [list_a[x]+list_b[y]
              for x in range(0, 2)
              for y in range(0, 2)
              if x == y]
    x = result[0]
    y = result[1]

    result_tuple = x, y
    return (result_tuple)
