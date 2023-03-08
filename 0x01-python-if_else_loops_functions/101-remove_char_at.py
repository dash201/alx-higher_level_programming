#!/usr/bin/python3
def remove_char_at(str, n):
    m = ""
    for c in range(0, len(str)):
        if c == n:
            m += ""
        else:
            m += str[c]
        return m
