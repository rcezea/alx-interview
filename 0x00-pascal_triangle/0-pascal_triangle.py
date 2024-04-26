#!/usr/bin/python3

"""
Create a function def pascal_triangle(n): that
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    triangle = []
    # if user input less than 1, print empty triangle
    if n <= 0:
        return triangle
    # loop for each layer[list] of the triangle[list of lists]
    for row in range(0, n):
        # create a list for current layer and populate "1" as default
        layer = [1] * (row + 1)

        """
        Since the first two lines of a pascal triangle don't require any
        logic, we can use the layer as created above e.g
        layer0 = [1] *(0 + 1) = [1], layer1 = [1] *(1 + 1) = [1]
        """

        # starting from row 2,
        if row > 1:
            # create a list that has the previous layer from the triangle
            pascal = triangle[row - 1]

            # Skipping the first and last elements so it stays as "1"
            for i in range(1, row):
                # run the pascal addition across for thr new layer
                layer[i] = pascal[i - 1] + pascal[i]
        # add the latest layer[list] to the triangle[list of lists]
        triangle.append(layer)

    return triangle
