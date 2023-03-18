#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = set()
    for c in set_1:
        if c in set_2:
            new.add(c)
    return new
