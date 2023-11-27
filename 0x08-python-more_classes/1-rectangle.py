#!/usr/bin/python3
"""
Defines a class Rectangle with private width and height
"""

class Rectangle:
    """
    Defines a Rectangle class
    """
    def __init__(self, width=0,height=0):
        """
        Initializes the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """
            Retrieves the width of rectangle
            """
            return self.__width

        @width.setter
        def width(self, num):
            """
            sets rectangle width
            """
            if not isinstance(num, int):
                raise TypeError("width must be an integer")
            if num < 0:
                raise ValueError("width must be >= 0")
            self.__width = num

        @property
        def height(self):
            """
            Retrieves the height rectangle
            """
            return self.__height

        @height.setter
        def height(self, num):
            """
            Sets height of rectangle
            """
            if not isinstance(num, int):
                raise TypeError("height must be an integer")
            if num < 0:
                raise ValueError("height must be >= 0")
            self.__height = num
