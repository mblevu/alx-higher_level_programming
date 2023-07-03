#!/usr/bin/python3
"""
Module:2-rectangle
empty class that defines a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The widht of the rectangle
            heigth(int) :The hight of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attrbute.
        Returns:
            int: The width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width value to set.
        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        Returns:
            int: The height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Args:
            value (int): The height value to set.
        Raises:
            TypeError: if the height is not an integer.
            ValueError: if the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns area of rectangle.
        Returns;
            int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates and returns the perimeter of rectangle.
        Returns:
            int: The perimeter of rectangle.
        """
        return (2 * (self.width + self.height))
