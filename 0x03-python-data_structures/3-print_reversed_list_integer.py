#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for c in reversed(my_list):
            print("{:d}".format(c))
