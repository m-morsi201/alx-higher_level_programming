#!/usr/bin/python3
"""
a class that defines a rectangle
"""

class Rectangle:
    """
    a class Rectangle that defines a rectangle method.

    Methods:
        width => it is width of the rectangle.
        height => it is height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
         Creates new instances of Class Rectangle.
         Arguments:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        method to Width retriver.

        Returns:
            the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        method to Height retriver.

        Returns:
            the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter method for width of rectangle.

        Argumets:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        setter method for height of recyangle.

        Arguments:
            value: the  height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
