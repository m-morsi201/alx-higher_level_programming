#!/usr/bin/puthon3
"""
Module with append_write() function.
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
        1. If the file doesn’t exist, it should be created.
        2. must use the with statement.
        3. don’t need to manage file permission or file doesn't exist.
    """
    with open(filename, "a", encoding="utf-8") as m:
        return m.write(text)
