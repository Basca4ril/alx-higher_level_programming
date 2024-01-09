#!/usr/bin/python3
"""Module for inherited list class"""


class MyList(list):
    """
    Prints sorted built-in class list
    """
    def print_sorted(self):
        """
        prints list in ascending order
        """
        print(sorted(self))
