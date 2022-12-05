#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    i = 1

    if list_len > 0:
        for i in reverse(my_list):
            print('{:d}'.format(my_list[i]))
