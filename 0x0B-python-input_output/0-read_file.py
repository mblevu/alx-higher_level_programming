#!/usr/bin/python3

"""Defines a text file-reading function."""


def read_file(filename=""):
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
    with open(filename, mode="r", encoding="utf-8") as file:
        content = file.read()
        print(content)
