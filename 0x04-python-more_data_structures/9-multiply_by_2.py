#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    res = {}
    for a in a_dictionary:
        res[a] = a_dictionary[a] * 2
    return res
