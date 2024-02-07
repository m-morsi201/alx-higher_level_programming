#!/usr/bin/python3
"""
Module that define load_from_json_file() function.
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a 'JSON file':
        1. must use the with statement.
    """
    with open(filename, "r", encoding="utf-8") as m:
        return json.load(m)
