#!/usr/bin/python3
"""
a function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    lookup module
    To return the list of available attributes we use a built-in dir() function.
    """
    return dir(obj)
