#!/usr/bin/python3
"""
Module that define pascal_triangle() function.
"""


def pascal_triangle(n):
    """
    function that returns a list of lists of
    integers representing the Pascal’s triangle of n:
        1. Returns an empty list if n <= 0
        2. n will be always an integer
    """
    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        tr = t[-1]
        m = [1]
        for item in range(len(tr) - 1):
            m.append(tr[item] + tr[item + 1])
        m.append(1)
        t.append(m)
    return t
