#!/usr/bin/python3

class Student:
    """A class representing a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names
        to be retrieved (default: None).

        Returns:
            dict: A dictionary containing the
        selected attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student
        instance based on a JSON dictionary.

        Args:
            json (dict): A dictionary representing
        the new attribute values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
