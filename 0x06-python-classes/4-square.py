#!/usr/bin/python4

"""
Definition of Square class
"""


class Square:
    """
    Square clas for square attributes and methods
    """
    def __init__(self, size=0):
        """
        Instantiates new clas

        Parameters:
        - size (int): Size of square
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves size

        Returns:
        - int: Size of square
        """
        return self.__size

    @size.setter
    def size(self, num):
        """
        Sets value for size

        Parameters:
        - num (int): Size

        Raises:
        - TypeError: If num is not an integer
        - ValueError: IF num is less that 0
        """
        if not isinstance(num, int):
            raise TypeError("size myst be an integer")

        if num < 0:
            raise ValueError("size must be >= 0")

        self.__size = num

    def area(self):
        """
        Calculates area of square

        Returns:
        - int: Area of the square
        """
        return self.__size * self.__size


if __name__ == "__main__":
    pass
