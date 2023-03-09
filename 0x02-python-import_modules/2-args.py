#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    size = len(argv) - 1
    i = 1
    if size == 0:
        print("{} arguments.".format(size))
    else:
        print("{} arguments:".format(size))
        while(i <= size):
            print("{}: {}".format(i, argv[i]))
            i += 1
