#!/usr/bin/python3
"""
Module that contain definition of class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    Definition of Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor with:
            width: width of rectangle.
            height: height of rectangle.
            x: Defaults to 0.
            y: Defaults to 0.
            id: the number of rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Width retriever to:
            Returns a width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width of rectangle that raise:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        method that return height:
            int: height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height of rectangle that raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        getter method for x, that returnsx.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x, that raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter method for y, that  returns: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y, that raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Function that returs the area of the Rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Function that prints in stdout the Rectangle instance with the character #.
        """
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()
