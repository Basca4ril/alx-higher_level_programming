#!/usr/bin/python3

"""
Definition of Square class
"""


class Square:
    """
    Square clas for square attributes and methods
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates new clas

        Parameters:
        - size (int): Size of square
        - position (tuple): Position of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieves position

        Returns:
        - tuple: position of square
        """
        return self.__position

    @position.setter
    def position(self, pos):
        """
        Sets value for position

        Parameters:
        - pos (tuple): position

        Raises:
        - TypeError: If value is not a tuple of positive integers
        """
        if not all(isinstance(i, int) and i >= 0 for i in pos):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = pos

    def area(self):
        """
        Calculates area of square

        Returns:
        - int: Area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints square with #

        0 if size is 0
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        String representation of square class

        Returns:
        - str: String representation
        """
        res = ""
        if self.__size == 0:
            res += "\n"

        else:
            for i in range(self.__position[1]):
                res += "\n"
            for i in range(self.__size):
                res += " " * self.__position[0] + "#" * self.__size + "\n"

        return res[:-1]


if __name__ == "__main__":
    pass
