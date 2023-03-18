#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    new = []
    for c in sorted(a_dictionary.item, reversed=True):
        new.append(c)
    return c[0]
