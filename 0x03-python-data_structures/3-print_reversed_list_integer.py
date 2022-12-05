#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    i = 1

    if list_len > 1:
        while i <= list_len:
            print('{:d}'.format(my_list[-1 * i]))
            i += 1
    else:
        print('{:d}'.format(my_list))
