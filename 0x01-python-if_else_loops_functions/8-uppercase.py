#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) in range(97, 123):
            s = chr(ord(s) - 32)
        print(s, end="")
    print(end="\n")
