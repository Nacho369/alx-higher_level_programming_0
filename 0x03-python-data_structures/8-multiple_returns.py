#!/usr/bin/python3


def multiple_returns(sentence):

    first_char = sentence[0]
    str_len = len(sentence)

    if sentence == "":
        new_tuple = (0, None)
        return (new_tuple)
    
    new_tuple = (str_len, first_char)
    return (new_tuple)
