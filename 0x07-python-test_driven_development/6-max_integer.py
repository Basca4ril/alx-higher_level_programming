#!/usr/bin/python3
"""
Module for max_integer function.
"""


def max_integer(lst=[]):
    """
    Returns the max integer from a list of integers.

    Args:
        lst (list): List of integers.

    Returns:
        int: The maximum integer in the list.

    Raises:
        ValueError: If the list is empty.
        TypeError: If the elements in the list are not integers.
    """
    if not lst:
        raise ValueError("list is empty")

    if not all(isinstance(x, int) for x in lst):
        raise TypeError("list must contain only integers")

    return max(lst)

