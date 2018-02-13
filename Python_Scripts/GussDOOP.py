import numpy as np


def ref(matrix):

    # FIND MATRIX LENGTH
    matrix_dimensions = np.shape(matrix)
    row_length = matrix_dimensions[0]
    col_length = matrix_dimensions[1]

    # STARTS AT 1 AND SORTS BELOW 0'S
    for column in range(col_length):
        for row in range(row_length):
            if column == row:
                matrix[row] = matrix[row] / matrix[row, column]
            elif column <= row:
                reduce_to_zero(row, column, row_length, matrix)

    # STOP NEGATIVE 0'S
    for i in range(row_length):
        for j in range(col_length):
            if matrix[i, j] == -0:
                matrix[i, j] = 0

    return matrix


def reduce_to_zero(row_start, col_to_change, row_length, matrix):
    for i in range(row_start, row_length):
        matrix[i] = matrix[i] + (-matrix[i,col_to_change] * matrix[col_to_change])


def solve_matrix(augmented_matrix):

    # FIND COLUMN LENGTH
    matrix_dimensions = np.shape(augmented_matrix)
    col_length = matrix_dimensions[0]

    # PRINT MATRICES FOR SOLUTIONS
    solution_matrix = augmented_matrix[:,col_length]
    print("Solution Matrix: \n", solution_matrix)

    # PRINT NEW R.E.F MATRIX
    augmented_matrix = np.delete(augmented_matrix, col_length, axis=1)
    print("REF Matrix: \n", augmented_matrix)

    # RETURN SOLUTIONS
    return np.linalg.solve(augmented_matrix, solution_matrix)
