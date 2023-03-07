#!/usr/bin/python3
for number in range(97, 123):
    if chr(number) != "e" or chr(number) != "q":
        print("{}".format(chr(number)), end="")
