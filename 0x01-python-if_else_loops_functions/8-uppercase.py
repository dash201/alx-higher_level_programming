#!/usr/bin/python3
def myupper(c):
    if ord(c) in range(97, 123):
        return chr(ord(c) - 32)
    else:
        return c


def uppercase(str):
    i = 0
    m = ""
    while (i < len(str)):
        if (i == len(str) - 1):
            m += myupper(str[i])
        else:
            m += myupper(str[i])
        i += 1
    print("{:s}".format(m))
