#!/usr/bin/python3

def multiple_returns(sentence):
        s_len = len(sentence)
        if s_len == 0:
                s_tuple = 0, None
                return s_tuple
        s_tuple = s_len, sentence[0]
        return s_tuple
