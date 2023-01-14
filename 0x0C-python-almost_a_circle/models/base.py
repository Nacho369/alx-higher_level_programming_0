#!/usr/bin/python3

"""Define a Base class"""

import json


class Base:
    """Represnt a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        This function returns the JSON string representation of
        list_dictionaries

        Args:
            list_dictionaries: Is a list of dictionaries

        Return: "[]" if list_dictionaries is None or empty
                else return the JSON string representation of
                list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
