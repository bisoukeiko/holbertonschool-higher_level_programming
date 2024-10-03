#!/usr/bin/python3
"""
    task12
"""


def pascal_triangle(n):
    """ Define a function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1 for col in range(row)] for row in range(1, n + 1)]

    for row in range(2, n):
        for col in range(1, row):
            triangle[row][col] = triangle[row-1][col] + triangle[row-1][col-1]

    return triangle
