#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    if list_len > 0:
        my_list = my_list[::-1]
        for i in my_list:
            print('{:d}'.format(i))
