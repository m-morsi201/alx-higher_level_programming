#!/usr/bin/python3
"""
Module that Defines a class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Definition of Square class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor that: creates new instances of Square.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size that returns:
            a size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for width of square, that raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ method should return [Square] (<id>) <x>/<y> - <size>.
        to Prints a square
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))
