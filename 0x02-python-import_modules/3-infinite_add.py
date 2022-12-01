#!/usr/bin/python3
def main(args):
    i = 1
    args_len = len(args)
    infinite_sum = 0

    while i < args_len:
        infinite_sum += int(args[i])
        i += 1
    print(infinite_sum)


if __name__ == "__main__":
    import sys
    main(sys.argv)
