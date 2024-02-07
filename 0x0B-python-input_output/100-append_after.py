#!/usr/bin/python3
"""
Module that define a append_after() function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    """

    with open(filename, "r") as m:
        t = m.readlines()

    with open(filename, "w") as f:
        r = ""
        for i in t:
            r += i
            if search_string in i:
                r += new_string
        f.write(r)
