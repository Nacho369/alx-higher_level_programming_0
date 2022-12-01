#!/usr/bin/python3

import sys


def main():
    argv = sys.argv
    n = 1

    args_len = len(argv)

    if (args_len == 1):
        print("{} {}".format(args_len - 1, "arguments."))
    elif (args_len == 2):
        print("{} {}".format(args_len - 1, "argument:"))
    elif (args_len > 2):
        print("{} {}".format(args_len - 1, "arguments:"))

    while (n < args_len):
        print("{}: {}".format(n, argv[n]))
        n += 1


if __name__ == '__main__':
    main()
