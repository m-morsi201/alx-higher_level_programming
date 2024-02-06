#!/usr/bin/python3
"""
Module which containing add_attribute method.
"""


def add_attribute(obj, name, value):
    """
    Method to check if attribute can be set and sets
    or not.
    """
    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
