#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        list_len = len(my_list)
        if list_len > 0:
            for i in reversed(my_list):
                print("{:d}".format(i), end="\n")
