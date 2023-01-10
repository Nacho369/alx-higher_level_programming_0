#!/usr/bin/python3

"""Defines the append_write() function"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename: Name of the file to append to
        text: Text to append to the file

    Return: Number of characters added
    """
    num_ch = 0

    with open(filename, "a", encoding="utf-8") as file_a:
        file_a.write(text)

        for ch in text:
            num_ch += 1

    return (num_ch)
