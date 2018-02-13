import numpy as np


def ref(matrix):

    # FIND MATRIX LENGTH
    matrix_dimensions = np.shape(matrix)
    row_length = matrix_dimensions[0]
    col_length = matrix_dimensions[1]

    # STARTS AT 1 ON DIAGONAL AND SORTS BELOW 0'S
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
        matrix[i] = matrix[i] + (-matrix[i, col_to_change] * matrix[col_to_change])


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


def create_two_by_two(points_before):

    new_matrix = np.array([
        [],
        [],
    ], dtype=float)

    array_row = []

    for i in range(0,2):
        point = points_before[i]
        point_x = point[0, 0]
        point_y = point[0, 1]
        array_row.append([point_x, point_y])

    new_matrix = np.append(new_matrix, array_row, axis=1)
    return new_matrix


def create_solutions(points_after):
    points = points_after[0]

    new_matrix = np.array([
        [],
        [],
    ], dtype=float)

    array_rows = []

    array_rows.append([points[0, 0]])
    array_rows.append([points[0, 1]])

    new_matrix = np.append(new_matrix, array_rows, axis=1)

    flipped_matrix = np.flip(new_matrix, axis=0)

    return [new_matrix, flipped_matrix]


def step_three(new_matrix, flipped_matrix, two_by_two):
    print("New Matrix \n", new_matrix)
    print("Flipped Matrix \n", flipped_matrix)
    print("Two by two: \n", two_by_two)

    new_one = np.append(two_by_two, new_matrix, axis=1)
    new_two = np.append(two_by_two, flipped_matrix, axis=1)

    return_matrix = np.array([
        [],
        [],
    ], dtype=float)

    add_list = []

    add_list.append(solve_matrix(new_one))
    add_list.append(solve_matrix(new_two))

    return_matrix = np.append(return_matrix, add_list, axis=1)

    return return_matrix


if __name__ == "__main__":

    # CREATE MATRIX
    aug_matrix = np.array([
        [1, 1, -1, 1],
        [8, 3, -6, 1],
        [-4, -1, 3, 1],
    ], dtype=float)

    # # WORKS
    # aug_matrix = np.array([
    #     [1, 1, -1, 1],
    #     [8, 3, -6, 1],
    #     [-4, -1, 3, 1],
    # ], dtype=float)

    print("Original Matrix: \n", aug_matrix)

    # PRODUCE R.E.F
    ref_matrix = ref(aug_matrix)
    print("REF Matrix: \n", ref_matrix)

    # SOLVE MATRIX
    print("Solutions \n", solve_matrix(ref_matrix))


    # new_matrix = np.append(aug_matrix, solutions, axis=1)
    # print("Joint Matrix: \n", new_matrix)

    ################################################################

    # POINTS BEFORE
    x = np.matrix(
        [[1., 2.],
         [2., 1.],
         [0., 3.],
         [2., 0.5]])

    # POINTS AFTER
    y = np.matrix(
        [[2.75, 3.25],
         [3.25, 2.75],
         [2.25, 3.75],
         [2.875, 2.125]])

    matrices = create_solutions(y)
    tm = step_three(matrices[0], matrices[1], create_two_by_two(x))
    print("Transition Matrix: \n", tm)





