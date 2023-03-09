#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    import re

    def Filter(data):
        return [val for val in data
                if not re.search(r'^_', val)]
    liste = dir()
    for c in Filter(liste):
        print("{}".format(c))
