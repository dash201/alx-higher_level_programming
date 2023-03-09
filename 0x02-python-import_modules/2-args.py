#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    l = len(argv) - 1
    i = 1
    if l == 0:
        print("{} arguments.".format(l))
    else:
        print("{} arguments:".format(l))
        while(i <= l):
            print("{}: {}".format(i, argv[i]))
            i += 1
