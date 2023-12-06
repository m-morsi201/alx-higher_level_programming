#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is str and roman_string:
        for i in range(len(roman_string)):
            if len(roman_string) == 2:
                if val[roman_string[i]] < val[roman_string[i + 1]]:
                    num = val[roman_string[i + 1]] - val[roman_string[i]]
                    return num
            else:
                num += val[roman_string[i]]
        return num
    else:
        return 0
