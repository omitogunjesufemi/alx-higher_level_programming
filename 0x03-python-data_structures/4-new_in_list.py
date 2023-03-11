#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_len = len(my_list)

    if idx < 0 or idx > list_len:
        return my_list
    else:
        for i in my_list:
            if my_list.index(i) == idx:
                new_my_list = my_list.copy()
                new_my_list[idx] = element
                return new_my_list
        return my_list
