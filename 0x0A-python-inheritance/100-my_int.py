#!/usr/bin/python3
"""
Module with MyInt class.
"""


class MyInt(int):
    """
    A class named  MyInt.
    """

    def __eq__(self, other):
        """
        method for Overides and inverts using == operator
        """

        return int(self) != int(other)

    def __ne__(self, other):
        """
        method for Overides and inverts using != operator
        """

        return int(self) == int(other)
