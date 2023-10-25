#!/usr/bin/python3
""" define a class Square """


class Square:
    """ define __init__ """
    def __init__(self, size=0):
        """ initializes size """
        self.size = size

    @property
    def size(self):
        """ returns __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ if statement """
        if type(value) is not int:
            """  error """
            raise TypeError("size must be an integer")
        elif value < 0:
            """  error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize """
            self.__size = value
    """ defines area """
    def area(self):
        """ returns area """
        return self.__size ** 2
