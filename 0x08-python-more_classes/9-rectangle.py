#!/usr/bin/python3
"""
Defines a class Rectangle with private width and height
"""

class Rectangle:
    """
    Defines a Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0,height=0):
        """
        Initializes the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculates area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates perimeter of rectangle
        """
        return 2 * (self.__width + self.__height) if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """
        Returns a string for printing
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([(str(self.print_symbol) * self.__width) for _ in range(self.__height)])
        
    def __repr__(self):
        """
        Returns string for recreation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints message when rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """
        Returns bigger rectangle
        """
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 msut be an isntance of Rectangle")

        area1 = rect1.area()
        area2 = rect2.area()

        if area1 >= area2:
            return rect1
        else:
            return rect2

    @classmethod
    def square(cls, size=0):
        """
        Returns new rectangle with width = height = size
        """
        return cls(size, size)
