#!/usr/bin/python3
"""
writes to file
"""


def write_file(filename="", text=""):
    """
    writes string to text file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        chars = file.write(text)

    return chars
