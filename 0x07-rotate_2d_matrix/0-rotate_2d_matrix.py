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
    matrix = [[matrix[i][j] for i in range(len(matrix))]
              for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        matrix[i].reverse()
