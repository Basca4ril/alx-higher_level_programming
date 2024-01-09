#!/usr/bin/python3
"""Module MyInt that inherits from int."""


class MyInt(int):
    """
    Inverts integer operators == and !=
    """

    def __eq__(self, val):
        """
        Overrides the == operator with != behavior
        """
        return self.num != val

    def __ne__(self, val):
        """
        Overrides the != operator with == behavior
        """
        return self.num == val
