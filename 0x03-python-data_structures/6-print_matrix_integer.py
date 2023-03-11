#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size_1 = len(matrix)
    for i in range(0, size_1):
        size_2 = len(matrix[i])
        for j in range(0, size_2):
            if j == size_2 - 1:
                print("{:d}".format(int(matrix[i][j])))
            else:
                print("{:d}".format(int(matrix[i][j])), end=" ")
