#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)

    if list_len > 0:
        for i in reversed(my_list):
            print("{}".format(i), end="\n")
