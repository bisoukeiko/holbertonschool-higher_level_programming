#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for index1 in range(len(matrix)):
        for index2 in range(len(matrix[index1])):
            print(matrix[index1][index2], end=" ")
            index2 += 1
        index1 += 1
        print()
