#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        char_ord = ord(ch)
        if (char_ord > 96 and char_ord < 123):
            char_up = char_ord - 32
            char_pr = chr(char_up)
            bools = True
        else:
            bools = False

        print("{}".format(char_pr if bools else ch), end="")

    print("")
