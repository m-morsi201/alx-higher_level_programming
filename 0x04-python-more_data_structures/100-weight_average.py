#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return sum(r * c for r, c in my_list) / sum(c for r, c in my_list)
    return 0
