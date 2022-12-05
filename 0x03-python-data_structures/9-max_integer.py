#!/usr/bin/python3


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)

    n = 0
    bigger_val = my_list[0]

    while n < len(my_list):
        if my_list[n] > bigger_val:
            bigger_val = my_list[n]

        n += 1

    return (bigger_val)
