#!/usr/bin/env python3
def no_c(my_string):
    m = list(my_string)
    for r in m:
        if r == 'c' or r == 'C':
            m.remove(r)
        return r
