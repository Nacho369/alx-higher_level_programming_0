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

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
