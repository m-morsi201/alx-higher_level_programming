#!/usr/bin/python3
def no_c(my_string):
    no_c_C = ""
    for m in range(len(my_string)):
        if my_string[m] != 'C' and my_string[m] != 'c':
            no_c += my_string[m]
        return (no_c)
