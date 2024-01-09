#!/usr/bin/python3
"""Module for object attribute lookup"""


def lookup(obj):
    """
    Returns list of available object attributes
    """
    return (dir(obj))
