#!/usr/bin/python3
"""
Checks if an object is an instance of a class inherited from class
"""


def inherits_from(obj, a_class):
    """
    Returns true if aninstance of a class is inherited from the classs
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
