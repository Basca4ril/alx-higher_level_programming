#!/usr/bin/python3
"""
Module for Mylist class to inherit from list
"""


class MyList(list):
    """
    Inherits from list
    """

    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
