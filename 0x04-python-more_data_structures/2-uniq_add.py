#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set(my_list[:])
    sum_list = 0

    for n in new_list:
        sum_list += n
    
    return (sum_list)
