#!/usr/bin/python3
"""
Module that define a Base class.
"""
import json
import os.path
import csv


class Base():
    """
    defination of base class with.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        defination of class constructo
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that returns the JSON string representation
        of list_dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method to writes the JSON string representation of list_objs to a file
        """
        fname = "{}.json".format(cls.__name__)
        dic_list = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                dic_list.append(list_objs[i].to_dictionary())

        ls = cls.to_json_string(dic_list)

        with open(fname, 'w') as f:
            f.write(ls)

    @staticmethod
    def from_json_string(json_string):
        """
        Static Method that returns the list of the JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with:
            all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            n = cls(1, 1)
        if cls.__name__ == "Square":
            n = cls(1)
        n.update(**dictionary)

        return(n)
