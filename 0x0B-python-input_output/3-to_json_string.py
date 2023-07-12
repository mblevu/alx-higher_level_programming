import json

"""returns JSON representation of an object"""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj (object): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.

    Raises:
        None

    """
    return (json.dumps(my_obj))
