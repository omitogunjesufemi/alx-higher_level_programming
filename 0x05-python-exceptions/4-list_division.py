#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ValueError:
            result = 0
            new_list.append(result)
        except ZeroDivisionError:
            result = 0
            new_list.append(result)
            print("division by 0")
        except TypeError:
            result = 0
            new_list.append(result)
            print("wrong type")
        except IndexError:
            result = 0
            new_list.append(result)
            print("out of range")
        finally:
            pass
    return new_list
