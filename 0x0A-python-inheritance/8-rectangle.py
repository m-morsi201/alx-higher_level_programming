#!/usr/bin/python3
"""
a class named Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Represent using BaseGeometry
    """

    def __init__(self, width, height):
        """
        Intialize a new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
