#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for c in range(len(matrix[row])):
            if c != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][column]), end='')
        print()
