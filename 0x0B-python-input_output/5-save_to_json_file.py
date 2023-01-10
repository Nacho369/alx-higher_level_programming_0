#!/usr/bin/python3

"""Define the save_to_json_file() function"""

import json


def save_to_json_file(my_obj, filename):
    """
    The function write an object to a text file using JSON
    representation.
    
    Args:
        my_obj: Object to convert
        filename: File to write converted object into
    """
    with open(filename, "w", encoding="utf-8") as file_w:
        json.dump(my_obj, file_w)
