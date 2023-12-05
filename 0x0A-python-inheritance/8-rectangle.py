#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """
    Class for base geometry
    """
    
    def area(self):
        """
        Raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))

class Rectangle(BaseGeometry):
    """
    Rectangle
    """

    def __init__(self, width, height):
        """
        Initialises rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
