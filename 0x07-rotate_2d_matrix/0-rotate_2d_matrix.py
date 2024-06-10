#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix: list) -> None:
    """
    Rotate a nxn matrix 90 degrees
    :param matrix: nxn matrix
    :return: None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
