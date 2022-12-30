#!/bin/usr/python3

"""
Defines a fumction that divides all element of a matrix
"""


def matrix_divided(matrix, div):
    """
    The function divides all element of the matrix and return a new matrix of the divison

    Args:
        matrix (list): A list of lists of ints or floats.
        div(int | float): The divisor

    Raise:
        TypeError: If matrix is not a list of lists of integers or floats,
        TypeError: If each row if the matrix is nkt if the same size
        TypeError: If @div is not a number(integer or float)
        ZeroDivisionError: If @div is equal to zero

    Return: A new mattix of all divided values
    """
    new_matrix = []
    t_err1 = "matrix must be a matrix (list of lists) of integers/floats"
    t_err2 = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(t_err1)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(t_err1)
        if not (len(row) == len(matrix[0])):
            raise TypeError(t_err2)
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(t_err1)

            res = round((col / div), 2)
            new_row.append(res)
        new_matrix.append(new_row)

    return(new_matrix)
