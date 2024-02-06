#!/usr/bin/python3
"""
module that contain a class named BaseGeometry.
"""


class BaseGeometry():
    """
    class named a BaseGeometry with two method:
    1. area()
    2. integer_validator()
    """

    def area(self):
        """
        area() Method which is not implemented.
        it will raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value:
            1. name is always a string
            2. if value is not an integer: raise a TypeError exception:
                with the message <name> must be an integer
            3. if value is less or equal to 0:
                raise a ValueError exception with
                the message <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
