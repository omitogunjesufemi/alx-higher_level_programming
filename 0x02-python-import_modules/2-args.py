#!/usr/bin/python3
def main(array):
    len_of_array = len(array)
    num_of_arg = len_of_array - 1
    end_with = ""
    i = 1

    if num_of_arg == 0:
        end_with = "s."
    elif num_of_arg == 1:
        end_with = ":"
    elif num_of_arg > 1:
        end_with = "s:"
    print(f"{num_of_arg} argument{end_with}")

    while i < len_of_array:
        print(f"{i}: {array[i]}")
        i = i + 1


if __name__ == "__main__":
    import sys
    main(sys.argv)
