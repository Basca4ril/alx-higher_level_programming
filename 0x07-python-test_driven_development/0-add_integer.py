#!/usr/bin/python3
"""
Module to add 2 integers
"""

def add_integer(a, b=98):
    """
    adds 2 integers

    Args:
    a (int): Integer 1
    b (int): Integer 2

    Returns:
    int: Total of a + b

    Raises:
    TypeError: If a or b != int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
