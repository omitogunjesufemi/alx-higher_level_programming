#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_len = len(my_list)

    if idx < 0 or idx > list_len:
        return my_list
    else:
        for i in my_list:
            if my_list.index(i) == idx:
                my_list[idx] = element
                return my_list
        return my_list
