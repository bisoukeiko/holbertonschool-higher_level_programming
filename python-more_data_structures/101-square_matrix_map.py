#!/usr/bin/python3

def square_matrix_map(matrix=[]):

    def square(num):
        return num ** 2

    return list(map(lambda list_x: list(map(square, list_x)), matrix))
