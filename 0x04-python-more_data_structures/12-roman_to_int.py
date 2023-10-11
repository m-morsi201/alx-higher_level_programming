#!/usr/bin/python3
def roman_to_int(roman_string):
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    s = 0

    if type(roman_string) is str and roman_string:
        for f in range(len(roman_string) - 1, -1, -1):
            if v[roman_string[f]] >= s:
                r += v[roman_string[f]]
            else:
                r -= v[roman_string[f]]
            s = v[roman_string[f]]
    return r
