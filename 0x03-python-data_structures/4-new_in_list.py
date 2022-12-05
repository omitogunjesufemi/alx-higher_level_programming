#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    new_list = [] + my_list
    i = 0

    if idx < 0 or idx > list_len:
        return my_list

    while i < list_len:
        if i == idx:
            new_list[i] = element
        else:
            new_list[i] = my_list[i]
        i += 1
    return new_list
