#!/usr/bin/python3
"""
Module with class named Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class with two method
    """
    def __init__(self, size):
        """
        Method for initializing a square method
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Method for  returns area of a square
        """

        return self.__size ** 2
