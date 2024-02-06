#!/usr/bin/python3
"""
a class MyList that inherits from list:
    1. Public instance method:
        that prints the list, but sorted (ascending sort).
    2. all the elements of the list will be of type int.
    3. not allowed to import any module.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """
    def print_sorted(self):
        """
        a public method that prints the list in ascending sort.
        """
        print(sorted(self))
