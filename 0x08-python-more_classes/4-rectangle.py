#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Class that defines method of rectangle with two methods.

    Methods:
        width of the rectangle.
        height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Creates new instances of Rectangle.

        Arguments:
            width of rectangle. Defaults to zero.
            height of rectangle. Defaults to zero.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Method for Width retrive.

        Returns:
            the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Methods for Height retrive.

        Returns:
            height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter Method for width of rectangle.

        Arguments :
            value: width of the rectangle.

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
        setter methd for height of recyangle.

        Arguments:
            value: height of the rectangle.

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
        method to Calculates area of a rectangle.

        Returns:
            area of rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Method to Calculates perimeter of a rectangle

        Returns:
            perimeter of rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Method to Prints the rectangle with the character # .

        Returns:
            The rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
