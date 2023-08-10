#!/usr/bin/python3
"""
Module containing the Rectangle class and integer_validator function.
"""

class BaseGeometry:
    """
    Class with area method.
    """

    def area(self):
        """
        Calculates the area.
        """
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """
        Validates the value to be a positive integer.
        """
        if type(value) is not int or value <= 0:
            raise ValueError("{} must be an integer greater than 0".format(name))


class Square(Rectangle):
    """
    Class representing a square.
    """

    def __init__(self, size):
        """
        Initializes a square with the given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

