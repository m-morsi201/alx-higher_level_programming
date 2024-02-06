#!/usr/bin/python3
"""
Module with write_file() function.
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written:
        1. must use the with statement
        2. need to manage file permission exceptions.
        3. function should create the file if doesn’t exist
        4. function should overwrite the content of the file
            if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as m:
        return m.write(text)
