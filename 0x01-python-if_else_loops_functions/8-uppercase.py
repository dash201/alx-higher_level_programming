#!/usr/bin/python3
def myupper(c):
    if ord(c) in range(97, 123):
        return chr(ord(c) - 32)
    else:
        return c


def uppercase(str):
    i = 0
    while (i < len(str)):
        if (i == len(str) - 1):
            print("{:s}".format(myupper(str[i])))
        else:
            print("{:s}".format(myupper(str[i])), end="")
        i += 1
