#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """
    Class that defines methods of rectangle.

    Methods:
        width of the rectangle.
        height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Creates new instances of Rectangle.

        Arguments:
            width: width of rectangle. Defaults to 0.
            height: height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        method for Width retriver.

        Returns:
            the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        method for Height retriver.

        Returns:
            the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter method for width of rectangle.

        Arguments:
            width of the rectangle.

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
            height of the rectangle.

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

    def area(self):
        """
        methods to Calculates area of a rectangle.

        Returns:
            area of rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        methods for Calculates perimeter of a rectangle

        Returns:
        perimeter of rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """

        Returns:
            str: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)
