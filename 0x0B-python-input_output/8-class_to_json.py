#!/usr/bin/python3
"""Module for a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description for JSON serialization.
    """
    return obj.__dict__
