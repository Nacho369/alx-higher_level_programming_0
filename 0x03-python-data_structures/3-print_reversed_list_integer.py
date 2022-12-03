#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()

    n = 0

    while n < len(my_list):
        print("{:d}".format(my_list[n]))
        n += 1


if __name__ == "__main__":
    print_reversed_list_integer()
