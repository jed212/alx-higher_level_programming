#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    new_m = [row.copy() for row in matrix]
    for r in range(rows):
        for c in range(cols):
            new_m[r][c] = new_m[r][c] ** 2
    return new_m
