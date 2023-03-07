#!/usr/bin/python3
def myupper(c):
    if ord(c) in range(65, 91):
        return c
    elif ord(c) == 32:
        return c
    else:
        return chr(ord(c)-32)


def uppercase(str):
    i = 0
    while (i < len(str)):
        if (i == len(str) - 1):
            print("{:s}".format(myupper(str[i])))
        else:
            print("{:s}".format(myupper(str[i])), end="")
        i += 1
