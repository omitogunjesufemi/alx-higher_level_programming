#!/usr/bin/python3
"""This module is a script that adds all arguments to a Python list and then
save them to a file
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main(argv):
    """This is the entry point to the code
    """
    my_list = []
    filename = "add_item.json"
    for i in range(1, len(argv)):
        my_list.append(argv[i])

    with open(filename, "a", encoding="utf-8") as f:
        pass

    with open(filename, "r", encoding="utf-8") as f:
        f_content = f.read()
        if f_content != "":
            f_json = load_from_json_file(filename)
            my_list = f_json + my_list

    save_to_json_file(my_list, filename)
    result = load_from_json_file(filename)


if __name__ == "__main__":
    """This calls the entry point function to make the program work
    """
    import sys
    main(sys.argv)
