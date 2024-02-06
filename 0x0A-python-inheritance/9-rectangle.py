#!/usr/bin/python3
"""
a class named Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    a Rectangle class with 3 methods
    """

    def __init__(self, width, height):
        """
        to Initilize rectangle method
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Method that returns area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
