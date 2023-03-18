#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set()
    for c in set_1:
        if c not in set_2:
            new.add(c)
    for c in set_2:
        if c not in new and c not in set_1:
            new.add(c)
    return new
