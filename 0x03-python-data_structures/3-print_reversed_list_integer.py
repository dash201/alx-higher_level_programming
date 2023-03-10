#!/usr/bin/python3
if __name__ == "__main__":

    def print_reversed_list_integer(my_list=[]):
        size = len(my_list)
        for c in range(size - 1, -1, -1):
            print("{:d}".format(my_list[c]))
