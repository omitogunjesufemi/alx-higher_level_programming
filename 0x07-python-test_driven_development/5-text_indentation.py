#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] not in ['.', '?', ':']:
            if i != 0 and text[i - 1] in ['.', '?', ':']:
                continue
            print(text[i], end="")
        else:
            print("{}\n".format(text[i]))
