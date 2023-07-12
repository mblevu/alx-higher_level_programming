#!/usr/bin/python3

"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the file to read
    (default is an empty string).

    Returns:
        None

    Raises:
        None

    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return (len(text))
