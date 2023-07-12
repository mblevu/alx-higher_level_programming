#!/usr/bin/python3

"""
returns a list of integers
representing pascal triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: The Pascal's triangle represented
    as a list of lists of integers.
    """
    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])

    for row in range(1, n):
        current_row = [1]

        for i in range(1, row):
            value = triangle[row - 1][i] + triangle[row - 1][i - 1]
            current_row.append(value)

        current_row.append(1)
        triangle.append(current_row)

    return triangle
