#!/bin/usr/python3

"""Define the function `text_indentation(text)`"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(str): Text to print with 2 new lines after the given characters

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_line = ""
    prev_ch = None

    for curr_ch in text:

        if not (curr_ch == " " and prev_ch in ".?:"):
            text_line += curr_ch

        if curr_ch in ".?:":
            print("{}".format(text_line))
            print("")
            text_line = ""

        prev_ch = curr_ch
