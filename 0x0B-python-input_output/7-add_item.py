#!/usr/bin/python3
"""Script to add arguments to a Python list and save them to a file."""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item():
    """
    Adds all command line arguments to a Python list and saves them to a file.
    """
    try:
        existing_items = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_items = []

    new_items = sys.argv[1:]

    all_items = existing_items + new_items

    save_to_json_file(all_items, "add_item.json")
