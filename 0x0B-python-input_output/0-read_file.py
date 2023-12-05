#!/usr/bin/python3
"""
reads file
"""


def read_file(filename=""):
    """
    reads text file and prints to stdout
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        stre = file.read()
        print(stre, end='')
