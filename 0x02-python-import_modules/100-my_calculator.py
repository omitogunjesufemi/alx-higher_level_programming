#!/usr/bin/python3
def main(args):
    len_of_args = len(args)
    operators = ['+', '-', '*', '/']

    if len_of_args != 4:
        print(f"Usage: {args[0]} <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    operator = args[2]
    b = int(args[3])

    if operator == '+':
        result = add(a, b)
        print(f"{a:d} {operator} {b:d} = {result:d}")
    elif operator == '-':
        result = sub(a, b)
        print(f"{a:d} {operator} {b:d} = {result:d}")
    elif operator == '*':
        result = mul(a, b)
        print(f"{a:d} {operator} {b:d} = {result:d}")
    elif operator == '/':
        result = div(a, b)
        print(f"{a:d} {operator} {b:d} = {result:d}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    main(sys.argv)
