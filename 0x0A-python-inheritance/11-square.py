#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Sqaure(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
        size (int): The size othe new square.
        """

        self.integer_validator("size", size)
            suoer().__init__(size, size)
            self.__size = size
