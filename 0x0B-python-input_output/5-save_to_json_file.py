#!/usr/bin/python3
"""
Module that define save_to_json_file() function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation:
        1. use the with statement.
    """
    with open(filename, "w", encoding="utf-8") as m:
        jsonObj = json.dumps(my_obj)
        return m.write(jsonObj)
