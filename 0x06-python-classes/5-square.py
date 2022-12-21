#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent  a square"""

    def __init__(self, size=0):
        """
        Initialize a new square
        Args:
            size(int): Size of square
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size if the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size if the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints to the stdout the square with the character "#" """
        if self.__size == 0:
            print("")

        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print("")
