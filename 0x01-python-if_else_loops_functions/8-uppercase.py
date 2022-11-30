#!/usr/bin/python3
def uppercase(str):
    for s in str:
        ascii_int = ord(s)
        if ascii_int in range(97, 123):
            ascii_int = ascii_int - 32
            print('{:c}'.format(ascii_int), end="")
        else:
            print('{:c}'.format(ascii_int), end="")
    print('{:c}'.format(10), end="")
