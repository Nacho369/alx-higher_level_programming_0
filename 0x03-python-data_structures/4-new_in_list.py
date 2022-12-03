#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list_cp = my_list[:]

    if idx < 0:
        return (my_list)

    if idx > len(my_list) - 1:
        return (my_list)

    new_list_cp[idx] = element
    return (new_list_cp)
