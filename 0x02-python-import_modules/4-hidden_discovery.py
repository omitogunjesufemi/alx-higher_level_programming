#!/usr/bin/python3
import hidden_4
import sys


def main():
    for i in dir(hidden_4):
        if i[0] == "_":
            continue
        print(i)


if __name__ == "__main__":
    main()
