#!/usr/bin/python3

def multiple_returns(sentence):
    s_len = len(sentence)
    if s_len == 0:
        return None

    s_tuple = s_len, sentence[0]
    return s_tuple
