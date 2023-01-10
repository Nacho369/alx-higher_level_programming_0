#!/usr/bin/python3

"""Define the save_to_json_file() function"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as file_w:
        json.dump(my_obj, file_w)
