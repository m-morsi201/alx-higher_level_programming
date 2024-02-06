#!/usr/bin/python3
"""
function that returns the list of all attributes and methods of an object.
"""


def lookup(obj):
    """
    lookup module.
    return the list of available attributes we use a built-in dir() function.
    """
    return dir(obj)
