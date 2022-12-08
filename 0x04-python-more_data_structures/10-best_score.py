#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    f_key = list(a_dictionary.keys())[0]
    big_val = a_dictionary[f_key]
    for key, value in a_dictionary.items():
        if value > big_val:
            big_val = value
            f_key = key

    return (f_key)
