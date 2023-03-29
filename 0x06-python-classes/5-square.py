#!/usr/bin/python3
"""A class  """


class Square:
    "Class Square definition"
    def __init__(self, size=0):
        self.__size = size
    """returns the current square area"""
    def area(self):
        return (self.__size ** 2)

    """getter"""
    @property
    def size(self):
        return self.__size

    """setter"""
    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """ prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size > 0:
            for n in range(self.__size):
                for i in range(self.__size):
                    if i < self.__size - 1:
                        print("#", end="")
                    else:
                        print("#", end="\n")
        else:
            print("")
