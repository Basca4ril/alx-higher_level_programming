#!/usr/bin/python3
"""Module for a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object represented by the JSON string.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
