#!/usr/bin/python3

"""Defines an inherited list class MyList."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of the specified class or a subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)
