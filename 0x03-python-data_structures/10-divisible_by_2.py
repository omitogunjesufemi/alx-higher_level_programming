#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    if len(my_list) > 0:
        for i in my_list:
            if i % 2 == 0:
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list
