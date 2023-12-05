#!/usr/bin/python3
"""
appends to text file
"""


def append_write(filename="", text=""):
    """
    appends string to text file
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        chars = file.write(text)

    return chars
