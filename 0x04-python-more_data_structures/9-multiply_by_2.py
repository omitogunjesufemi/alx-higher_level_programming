#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()

    for x, y in new_dic.items():
        y = y * 2
        new_dic[x] = y
    return new_dic
