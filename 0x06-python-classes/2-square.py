#!/usr/bin/python3

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


if __name__ == "__main__":
    pass
