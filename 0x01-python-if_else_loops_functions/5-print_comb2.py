#!/usr/bin/python3
i = 0
j = 0
while (i < 10):
    if (i == 9 and j == 9):
        print("{}{}".format(i, j), end="\n")
    else:
        print("{}{}".format(i, j), end=", ")
    i = i + 1
    j = j + 1
