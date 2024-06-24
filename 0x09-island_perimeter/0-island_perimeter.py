#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Find the perimeter of an island
    :param grid:
    :return: grid perimeter
    """
    def check_left_right(i, j):
        """ check for land on the horizontal axis"""
        edge = 0
        if j - 1 < 0 or grid[i][j - 1] == 0:
            edge += 1
        if j+1 > (len(grid[i]) - 1) or grid[i][j + 1] == 0:
            edge += 1
        return edge

    def check_top_bottom(i, j):
        """ check for land on the vertical axis"""
        edge = 0
        if (i - 1) < 0 or grid[i - 1][j] == 0:
            edge += 1
        if (i + 1) > (len(grid) - 1) or grid[i + 1][j] == 0:
            edge += 1

        return edge

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += check_left_right(i, j)
                perimeter += check_top_bottom(i, j)
    return perimeter
