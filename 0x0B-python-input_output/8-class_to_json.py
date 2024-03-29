#!/usr/bin/python3
"""
Module that define class_to_json() function.
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
        1. obj is an instance of a Class.
    """
    return obj.__dict__
