#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """
    Prevents user from dynmically creating new instance attributes except
    if the new instance attribute is called first_name
    """
    __slot__ = ('first_name',)
