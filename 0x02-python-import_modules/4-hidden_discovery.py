#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    list1 = dir()
    list2 = []
    for c in list1:
        if "__" not in c:
            list2.append(c)
    for c in sorted(list2):
        print("{}".format(c))
