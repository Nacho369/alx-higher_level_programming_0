#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for dicts in sorted(a_dictionary):
        print("{:s}: {}".format(dicts, a_dictionary[dicts]))
