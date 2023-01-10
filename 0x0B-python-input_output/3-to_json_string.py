#!/usr/bin/python3

"""Defines the to_json_string() function"""

import json


def to_json_string(my_obj):
    """
    The function returns the JSON representation of an object (string)
    
    Args:
        my_obj(str): Object

    Return: JSON representation of my_obj
    """
    return (json.dumps(my_obj))
