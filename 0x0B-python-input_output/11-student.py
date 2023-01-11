#!/usr/bin/python3

"""Defines a Student class"""


class Student:
    """Creates a Student class"""

    def __init__(self, first_name, last_name, age):
        """
        Instantiate the Student class

        Args:
            first_name: Student first name
            last_name: Student last name
            age: Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        my_dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    my_dict = self.__dict__
                    break
                try:
                    my_dict[i] = getattr(self, i)
                except Exception:
                    pass
        else:
            my_dict = self.__dict__
        return (my_dict)

    def reload_from_json(self, json):
        """
            Replaces all attributes of student instance
        """
        for key, val in json.items():
            self.__setattr__(key, val)
