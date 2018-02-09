import numpy as np

# x = np.mat("2 -1 2; 1 -2 1; 3 -1 2")
# x = np.matrix([
#  [ 2,  -1, 2],
#  [ 1,  -2, 1],
#  [3, -1, 2]], dtype='float')

test_matrix = np.array([
    [2,-1,2],
    [1,-2,1],
    [3,-1,2],
],dtype=np.float)

large_matrix = np.array([
    [2,-1,2,1],
    [1,-2,1,1],
    [3,-1,2,1],
    [3,-1,2,1],
],dtype=np.float)

solutions = np.array([10,8,11])


def ref(matrix, array):

    # Find length of matrix
    length = int(matrix.size ** 0.5)

    # if not == 1 make it = 1
    if matrix[0, 0] != 1:
        make_first_item_one(matrix, array)

    print("Updated, changed [0,0] to equal 1: \n", matrix)

    # Check remaining values on first row
    multipliers = check_column(matrix, array, length, 0, 1)      # multipliers  = [[value, row],[value, row]]
    print("Multipliers: ", multipliers)

    for multiplier in multipliers:
        matrix[multiplier[1]] = matrix[multiplier[1]] - multiplier[0] * matrix[0]
        # row = row- (multiplier * value in column one)

    print("Updated, changed all rows below row 0 on first column: \n", matrix)

    # NEXT STEP DEAL WITH THE -1.5 ON ROW 2, INDEX[1]


def make_first_item_one(matrix, array):
    """
    Makes item at position [0,0] in a matrix equal to 1
    :param matrix: matrix of values
    :param array: array of solutions to matrix
    :param length: length of a square matrix
    :return:
    """

    # Find multiplier needed to make [0,0] = 1
    multiplier = 1 / matrix[0, 0]

    # Update values on row
    matrix[0] = matrix[0] * multiplier

    # Update solution value
    array[0] = array[0] * multiplier


def check_column(matrix, solutions, length, column, row_start = 0):
    """
    Given a starting row, check all values below in the given column
    :param matrix: Matrix of values
    :param solutions:
    :param length: Length of square matrix
    :param column: Column to check values from
    :param row_start: Inclusive, starting row
    :return: A list of arrays containing [value found, row number]
    """

    values_below = []

    for row in range(length):
        if row_start > row:
            continue
        values_below.append([matrix[row, column], row])

    return values_below


def minus_row_ones(matrix, row_number, row_ones):
    print()


if __name__ == "__main__":
    print("Original Matrix: \n", test_matrix)
    ref(test_matrix, solutions)
