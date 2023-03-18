#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    new = []
    for c in a_dictionary:
        new.append(a_dictionary[c])
    return max(new)
