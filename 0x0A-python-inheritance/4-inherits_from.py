#!/usr/bin/python3
"""
module that Contains function that compares an object with an instance.
"""


def inherits_from(obj, a_class):
    """
     function that returns True if:
        the object is an instance of a class that inherited from the a class
     otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
