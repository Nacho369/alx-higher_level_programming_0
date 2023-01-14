#!/usr/bin/python3

"""Define a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square class that inherits from a Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square class wiyh its arguments
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overwritting the ste method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
