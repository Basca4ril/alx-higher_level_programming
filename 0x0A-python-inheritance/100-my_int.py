#!/usr/bin/python3
"""
MyInt
"""


class MyInt(int):
    """
    MyInt
    """

    def __eq__(self, other):
        """
        equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        not equal
        """
        return super().__eq__(other)
