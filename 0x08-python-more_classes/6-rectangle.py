#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    class rectangle that define a rigtangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        width of regtangle.
        """
        return self.__width

    @property
    def height(self):
        """
        height of regtangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter method to set width of regtangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter method to set height of regtangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        method to returns rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method to returns a rectangle perimiter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        method to return the rectangle with the character #.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """
        Method to return a string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        method to Print the message after  an instance of Rectangle is deleted.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
