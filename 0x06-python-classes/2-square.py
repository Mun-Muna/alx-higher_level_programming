#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    This is a class defining the structure of a square.

    Attributes:
        __size (int): Private instance attribute
            representing size of the square.
    """

    def __init__(self, size=0):
        """
        Initialises an instance of the square class.

        Args:
            size (int): The size of the square.
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
