#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        column = len(row)
        for i in range(column):
            print("{:d}".format(row[i]), end=' ' if i < column - 1 else '\n')
