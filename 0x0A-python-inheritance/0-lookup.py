#!/usr/bin/python3
"""
Module with function to gets attributes and methods
"""


def lookup(obj):
    """
    returns list of available attributes and methods of an object

    Args:
    obj: Object

    Returns:
    List of names of attributes and methods
    """
    return dir(obj)
