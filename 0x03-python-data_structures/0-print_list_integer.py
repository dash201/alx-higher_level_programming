#!/usr/bin/python3
def print_list_integer(my_list=[]):
    size = len(my_list)
    for i in range(0, size):
        print("{:d}".format(int(my_list[i])))
