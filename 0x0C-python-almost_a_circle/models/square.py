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
        """Overwritting the str method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Get the size of the square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the class Square to assign attributes

        Args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        """
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        if not args or len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return 
