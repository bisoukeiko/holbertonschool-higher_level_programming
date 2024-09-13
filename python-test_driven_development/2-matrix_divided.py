#!/usr/bin/python3

""" function that divide all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix is empty.
        TypeError: If the matrix and row_list are not a list.
        TypeError: If the element of row_list are not a int or float.
        TypeError: If each row_list of the matrix dosen't have the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Return:
        A new matrix with the result of the division.
    """

    errormessage = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(errormessage)

    if all(type(row_list) is not list for row_list in matrix):
        raise TypeError(errormessage)

    for row_list in matrix:

        if len(row_list) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for num in row_list:
            if type(num) not in [int, float]:
                raise TypeError(errormessage)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda num: round(num / div, 2), row)) for row in matrix]
