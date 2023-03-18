#!/usr/bin/python3

def weight_average(my_list=[]):
    part = 0
    di = 0
    res = 0
    for a in my_list:
        part = part + (a[0] * a[1])
        di = di + a[1]
    res = part / di
    return res
