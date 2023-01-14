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

    @staticmethod
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

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list of the JSON string representation
        json_string

        Args:
            json_string: Is a string representing a list of dictionaries

        Return: "[]" if json_string is None or empty
                else return list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return ("[]")
        else:
            return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes the JSON string representation of list_objs
        to a file

        Args:
            list_objs: Is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        content = []

        with open(filename, "w") as file_w:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                for item in list_objs:
                    item = item.to_dictionary()
                    json_dict = json.loads(cls.to_json_string(item))
                    content.append(json_dict)

            json.dump(content, file_w)
