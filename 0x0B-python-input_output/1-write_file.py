#!/usr/bin/python3

"""Defines the function write_file() that writes to a file"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename: Name of the file to write to
        text: Text to be written into the file

    Return: Number of characters in the file
    """
    num_ch = 0

    with open(filename, "w", encoding="utf-8") as file_w:
        file_w.write(text)

    with open(filename, encoding="utf-8") as file_r:
        for line in file_r:
            for ch in line:
                num_ch += 1

    return (num_ch)
