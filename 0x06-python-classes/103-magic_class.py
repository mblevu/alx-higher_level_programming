#!/usr/bin/python3
"""
Module: 103-magic_class.py
Class Node that defines a node of a singly linked list.
Class SinglyLinkedList that defines a singly linked list.
"""


class MagicClass:
    """
    A class that represents a magic circle with radius.

    Attributes:
        __radius (float): The radius of the magic circle.
    """

    def __init__(self, radius):
        """
        Initializes a MagicClass instance with the given radius.

        Args:
            radius (float): The radius of the magic circle.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return (2 * math.pi * self.__radius ** 2)
    
    def circumference(self):
        """
        Calculates the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return (2 * math.pi * self.__radius)
