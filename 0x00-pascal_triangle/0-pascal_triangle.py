#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates a list of lists of integers representing the Pascal's triangle of n.

    Parameters:
    n (int): The number of rows to generate for the Pascal's triangle.

    Returns:
    list of lists of integers: A list of n lists, where the ith list contains i+1 integers representing the ith row of the Pascal's triangle. Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
