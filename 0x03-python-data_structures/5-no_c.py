#!/usr/bin/python3
def no_c(my_string):
    with_out_Cc = ""
    for m in range(len(my_string)):
        if (my_string[m] != 'c' and my_string[m] != 'C'):
            with_out_Cc += my_string[m]
    return with_out_Cc
