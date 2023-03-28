#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for n in my_list:
            if i < x:
                print("{}".format(n), end="")
                i += 1
        print("")
        return i
    except ValueERROR as err:
        print("{}".format(err))
