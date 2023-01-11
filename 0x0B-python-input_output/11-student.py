#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_nmae
        self.last_nmae = last_nmae
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes included in the list.
        Args:
            attrrs (list): (optional) The attributes to represent.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getrattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replace all attributes of the student.
        Args:
        json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
