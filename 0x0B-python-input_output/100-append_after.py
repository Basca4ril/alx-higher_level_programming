#!/usr/bin/python3
"""Module for a function to insert a line of text after each line containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to be inserted after each line containing the search string.

    Returns:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, mode="w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
