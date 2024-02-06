#!/usr/bin/python3
"""
Module with read_file() function.
"""


def read_file(filename=""):
    """
     function that reads a text file (UTF8) and prints it to stdout:
        1. must use the with statement.
        2. don’t need to manage file permission or file doesn't exist.
    """
    with open(filename, "r", encoding="utf-8") as m:
        print(m.read(), end="")
