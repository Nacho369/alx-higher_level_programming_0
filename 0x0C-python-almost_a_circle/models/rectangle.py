#!/usr/bin/python3

"""Define a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    Represent a Rectangle class that inherits from a Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @staticmethod
    def validate_attr(attr, val):
        """
        Validate the setter methods based on the attr and val given

        Raise:
            TypeError: If val is not an int
            ValueError: If val is less than Zero

        Args:
            attr: Attribute to be passed
            val: Value to be passed
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format(attr))
        if attr == "x" or attr == "y":
            if val < 0:
                raise ValueError("{} must be >= 0".format(attr))
        elif val <= 0:
            raise ValueError("{} must be > 0".format(attr))

    @property
    def width(self):
        """Get width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, val):
        """Set width of the rectangle"""
        self.validate_attr("width", val)
        self.__width = val

    @property
    def height(self):
        """Get height if rectangle"""
        return (self.__height)

    @height.setter
    def height(self, val):
        """Set height of rectangle"""
        self.validate_attr("height", val)
        self.__height = val

    @property
    def x(self):
        """Get x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        """Set x of the rectangle"""
        self.validate_attr("x", val)
        self.__x = val

    @property
    def y(self):
        """Get y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, val):
        """Set y of the rectangle"""
        self.validate_attr("y", val)
        self.__y = val

    def area(self):
        """
        The function returns the area value of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """The function prints in stdout the Rectangle instance
        with the character `#`"""

        for row in range(self.__height):
            for col in range(self.width):
                    print("#", end="")
            print("")
