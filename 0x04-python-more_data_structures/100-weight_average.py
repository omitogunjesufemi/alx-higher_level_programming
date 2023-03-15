#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0

    numerator = 0
    denominator = 0
    for tp in my_list:
        numerator += tuple_mul(tp)
        denominator += tp[1]

    avg = numerator / denominator
    return avg


def tuple_mul(tps):
    x, y = tps
    return x * y
