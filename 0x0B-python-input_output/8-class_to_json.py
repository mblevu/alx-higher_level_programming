#!/usr/bin/python3

"""returns the dictionary descripition"""


def class_to_json(obj):
    """
    returns a json representation of an object's __dict__.
    """
    return (obj.__dict__)
