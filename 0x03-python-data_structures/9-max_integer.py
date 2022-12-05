#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)

    if list_len > 0:
        max_int = my_list[0]
        for ints in my_list:
            if ints > max_int:
                max_int = ints
        return max_int
    else:
        return None
