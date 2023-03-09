#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main(argv):
    argv_len = len(argv[1:])
    result = 0

    if argv_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if operator == "+":
            result = a + b
        elif operator == "-":
            passresult = a - b
        elif operator == "*":
            passresult = a * b
        elif operator == "/":
            passresult = a / b
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, operator, b, result), end="\n")


if __name__ == "__main__":
    main(sys.argv)
