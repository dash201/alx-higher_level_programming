#!/usr/bin/python3
for c in range(0, 11):
        print("{:02d}".format(c), end=", ")
for c in range(11, 90):
    if c != 89:
        print(f"{:d}".format(c), end=", ")
    else:
        print(f"{:d}".format(c))
