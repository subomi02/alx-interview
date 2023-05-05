#!/usr/bin/python3
"""
0. alx interview pascals triangle
"""
def pascal_triangle(n):
    """Create a function that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    lis = []
    if n > 0:
        for i in range(1, n + 1):
            els = []
            C = 1
            for j in range(1, i + 1):
                els.append(C)
                C = C * (i - j) // j
            lis.append(els)
    return lis
