#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    size = len(my_string)
    for i in range(0, size):
        if my_string[i] in ["c", "C"]:
            new_str += ""
        else:
            new_str += my_string[i]
    return new_str
