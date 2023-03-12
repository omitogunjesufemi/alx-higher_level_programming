#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    i = list_len - 1

    if list_len > 0:
        while i != -1:
            print("{:d}".format(my_list[i]), end="\n")
            i -= 1
