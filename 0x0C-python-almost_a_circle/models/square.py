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

    def update(self, *args, **kwargs):
        """
        Function to assigns an argument to each attribute
        """

        if args is not None and\
                len(args) != 0:
            attr_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr_list[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method that representation of a Square.
        """

        attr_list = ['id', 'size', 'x', 'y']
        dict2 = {}

        for k in attr_list:
            if k == 'size':
                dict2[k] = getattr(self, 'width')
            else:
                dict2[k] = getattr(self, k)

        return dict2
