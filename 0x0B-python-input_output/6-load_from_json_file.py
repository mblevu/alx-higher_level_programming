#!/usr/bin/python3
import json

"""creates an object from a JSON file"""


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object created from the JSON file.

    Raises:
        None

    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return (data)
