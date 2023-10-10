#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for m in my_string:
        if m != 'C' or m != 'c':
            no_c += m
        return (no_c)
