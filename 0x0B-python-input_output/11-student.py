#!/usr/bin/python3
"""
Module that define a class named student.
"""


class Student():
    """
    a class that define methods of student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation of a Student.
        """

        if attrs is None:
            return self.__dict__

        newDict = {}
        for i in attrs:
            try:
                newDict[i] = self.__dict__[i]
            except Exception:
                pass
        return newDict

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of the Student instance.
        """

        self.__dict__.update(json)
