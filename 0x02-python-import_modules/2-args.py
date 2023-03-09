#!/usr/bin/python3
def main(args):
    args_len = len(args)
    i = 1
    ar = ""

    if args_len > 1:
        ar = "s"

    if args_len > 0:
        print("{} argument{}:".format(args_len, ar), end="\n")
        for arg in args:
            print("{}: {}".format(i, arg), end="\n");
            i = i + 1
    else:
        print("0 arguments.")


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
