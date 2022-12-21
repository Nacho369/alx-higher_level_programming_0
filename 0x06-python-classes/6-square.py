#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent  a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square
        Args:
            size(int): Size of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the current size if the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size if the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Get the """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints to the stdout the square with the character "#" """
        if self.__size == 0:
            print("")
            return

        for e in range(self.__position[1]):
            print("")

        for x in range(self.__size):
            for a in range(self.__position[0]):
                print(" ", end="")

            for y in range(self.__size):
                print("#", end="")
            print("")
