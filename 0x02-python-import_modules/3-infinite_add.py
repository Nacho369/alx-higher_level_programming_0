#!/usr/bin/python3

import sys

def main():
    argv = sys.argv
    arg_len = len(argv)
    n = 1
    sum_res = 0

    while (n < arg_len):
        sum_res += int(argv[n])
        n += 1

    print("{}".format(sum_res))
    


if __name__ == '__main__':
    main()
