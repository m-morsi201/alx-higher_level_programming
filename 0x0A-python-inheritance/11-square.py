#!/usr/bin/python3
"""
A Module that defines a Rectangle as subclass Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class named square with __init__ method and anther two methods.
    """

    def __init__(self, size):
        """
        Method for Initialize a new square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method that returns area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Method that returns a string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
