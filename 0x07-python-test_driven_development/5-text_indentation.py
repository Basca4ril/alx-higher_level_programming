#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    new_line = True

    for char in text:
        if new_line and char == ' ':
            continue
        print(char, end='')
        if char in special_chars:
            print('\n')
            new_line = True
        else:
            new_line = False

    print('')

