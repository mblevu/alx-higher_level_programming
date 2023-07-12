#!/usr/bin/python3
# 6-from_json_string.py
import json

"""
returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """
    Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to be
        converted to a Python data structure.

    Returns:
        object: The Python data structure
        represented by the JSON string.

    Raises:
        None

    """
    return (json.loads(my_str))
