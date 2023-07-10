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

    def integer_validator(self, name, value):
        """
        Validates the given value as an integer.
        Raises TypeError if value is not an integer.
        Raises ValueError if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
