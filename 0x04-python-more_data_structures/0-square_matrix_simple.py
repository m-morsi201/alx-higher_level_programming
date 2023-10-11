#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_mat = [[c ** 2 for c in r] for r in matrix]
    return n_mat
