#!/usr/bin/python3
import hidden_4


def main():
    defined_names = dir(hidden_4)
    for i in defined_names:
        if i[0] != "_":
            print(i)


if __name__ == "__main__":
    main()
