#!/usr/bin/python3
""" defines a class Square """


class Square:
    """ defines __init__ """
    def __init__(self, size=0):
        """ if statement """
        if type(size) != int:
            """ error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize __size """
            self.__size = size
