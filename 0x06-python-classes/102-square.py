#!/usr/bin/python3
"""
Module: 102-square.py
Class Node that defines a node of a singly linked list.
Class SinglyLinkedList that defines a singly linked list.
"""


class Square:
    """A class to represent the square."""

    def __init__(self, size=0):
        """
        Initialize a Square object.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve size of the square"""
        return (self._size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size value to be set.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return (self.size ** 2)

    def __eq__(self, other):
        """check is two squares are equal in terms of area"""
        if isinstance(other, Square):
            return (self.area() == other.area())
        return (False)

    def __ne__(self, other):
        """check is one square is less than another in terms of area"""
        if isinstance(other, Square):
            return (self.area() != other.area())
        return (True)

    def __lt__(self, other):
        """check if one square is less than or equal to
        another in terms of area"""
        if isinstance(other, Square):
            return (self.area() < other.area())
        return (False)

    def __le__(self, other):
        """check if one square is less than or equal to
        another in terms or area"""
        if isinstance(other, Square):
            return (self.area() <= other.area())
        return (False)

    def __gt__(self, other):
        """Check if one square is greater than another in terms of area."""
        if isinstance(other, Square):
            return (self.area() > other.area())
        return (False)

    def __ge__(self, other):
        """Check if one square is greater than or equal
        to another in terms of area."""
        if isinstance(other, Square):
            return (self.area() >= other.area())
        return (False)
