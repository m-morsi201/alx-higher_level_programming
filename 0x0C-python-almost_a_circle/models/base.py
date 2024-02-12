#!/usr/bin/python3
"""
Module that define a Base class.
"""


class Base():
    """
    defination of base class with.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        defination of class constructo
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
