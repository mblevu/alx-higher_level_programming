#!/usr/bin/python3

"""Defines a text append function."""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)
    and return the number of characters added.

    Args:
        filename (str): The name of the file to
        append to (default is an empty string).
        text (str): The string to append to the
        file (default is an empty string).

    Returns:
        int: The number of characters added.

    Raises:
        None

    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return (len(text))
