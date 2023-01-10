#!/usr/bin/python3

"""Define the read_file() function"""


def read_file(filename=""):
    """
    This function read a text file (UTF8) and prints it to stdout

    Args:
        filename: Name of the file to be created
        text: Text to be written into the file

    Return: Number of character written
    """
    with open(filename, encoding="utf-8") as file_n:
        file_r = file_n.read()
        print(file_r, end="")
