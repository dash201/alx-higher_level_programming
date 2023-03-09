#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    size = len(argv)
    i = 1
    add = 0
    while(i < size):
        add = add + int(argv[i])
        i += 1
    print("{:d}".format(add))
