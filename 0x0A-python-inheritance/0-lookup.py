#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes
    and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of available attributes and methods.
    """
    return [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute)) or attribute.startswith('__')]
