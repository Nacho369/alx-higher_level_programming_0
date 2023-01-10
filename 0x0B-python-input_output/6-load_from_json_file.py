#!/usr/bin/python3

"""Define the load_from_json_file() function"""

import json


def load_from_json_file(filename):
    """
    The function creates an Object from a “JSON file”

    Args:
        filename: File to read the json string from
    """

    with open(filename, "r", encoding="utf-8") as file_r:
        return (json.load(file_r))
