#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return None
    else:
        big_int = my_list[0]
        for i in range(0, size):
            if my_list[i] > big_int:
                big_int = my_list[i]
        return big_int
