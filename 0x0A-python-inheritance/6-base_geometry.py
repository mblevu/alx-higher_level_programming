#!/usr/bin/python3

"""Defines a class base geometry."""


class BaseGeometry:
    """
    Base class representing a base geometry.
    """

    def area(self):
        """
        Raises an exception with a message that area() is not implemented.
        """
        raise Exception("area() is not implemented")
