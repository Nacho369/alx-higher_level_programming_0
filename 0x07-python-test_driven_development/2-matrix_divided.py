#!/bin/usr/python3

"""
Defines a fumction that divides all element of a matrix
"""


def matrix_divided(matrix, div):
    new_matrix = []
    t_err1 = "matrix must be a matrix (list of lists) of integers/floats"
    t_err2 = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list):
        raise TypeError(t_err1)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(t_err1)
        if not (len(row) == len(matrix[0])):
            raise TypeError(t_err2)
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(t_err1)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

