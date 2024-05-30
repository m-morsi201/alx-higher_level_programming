#!/usr/bin/python3
"""
Module that Find a peak.
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    - not allowed to import any module.
    - algorithm must have the lowest complexity.
    """

    n = len(list_of_integers)
    m = int(n / 2)

    if list_of_integers == []:
        return None

    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    p = list_of_integers[m]

    if p > list_of_integers[m - 1] and p > list_of_integers[m + 1]:
        return p
    elif p < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])
