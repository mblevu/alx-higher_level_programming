#!/usr/bin/python3
"""
Module: 101-square.py
Class Node that defines a node of a singly linked list.
Class SinglyLinkedList that defines a singly linked list.
"""


class Square:
    """A class to represent the square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square object.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
        Defaults to (0, 0)..
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """"retrieve the size of the square."""
        return (self._size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """retrieve position of the square"""
        return (self._position)

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position value to be set.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def my_print(self):
        """print the square using the character '#'."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        string = ""
        if self.size == 0:
            return (string)

        for _ in range(self.position[1]):
            string += "\n"

        for _ in range(self.size):
            string += " " * self.position[0] + "#" * self.size + "\n"

        return (string.rstrip())
