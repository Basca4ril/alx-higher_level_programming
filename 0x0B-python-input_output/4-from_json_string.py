#!/usr/bin/python3
# 6-from_json_string.py
"""Module for a JSON-to-object function."""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
