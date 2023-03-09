#!/usr/bin/python3

def main(argv):
    argv_len = len(argv[1:])
    sum = 0

    if argv_len > 1:
        for arg in argv[1:]:
            arg = int(arg)
            sum = sum + arg
        print(sum)
    else:
        print(0)

if __name__ == "__main__":
    import sys
    main(sys.argv)
