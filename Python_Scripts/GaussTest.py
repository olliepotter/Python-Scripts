import numpy as np

y = np.array([
    [2,-1,2],
    [1,-2,1],
    [3,-1,2],
])

x = np.array([
    [1,-0.5,1],
    [1,-2,1],
    [3,-1,2],
])

print(x[0])
print(x[1])
print()
print(x[2]-3*(x[0]))

# for column in range(length):
    #     matrix[1, column] = matrix[1, column] - matrix[0, column]

    # matrix[1, 1] = matrix[1, 1] * 1 / -1.5
        # matrix[2, column] = matrix[2, column] - 3*matrix[0, column]


# CHECK 0,0 FOR 1 IF 1 CONTINUE
# CHECK FOR 1'S ON FIRST ROW

# LOOP Y'S STARTING AT 1 UP UNTIL N
# CALCULATE MULTIPLIER
# LOOP X'S FROM 0 TO N
# RECALCULATE TERM MULTIPLIER X TERM
# for row in range(int(matrix.size**0.5)):
#     print(matrix[row,0])