#!usr/bin/python3

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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
