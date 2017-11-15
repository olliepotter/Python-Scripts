import matplotlib.pyplot as plt
from random import *


def logistic_map(initial_condition, steps=100, p=3.0):
    """
    Creates a list of y coordinates which can be used to plot a logistic map

    :param initial_condition: Random number between 0 and 1 used
        as a starting point
    :param steps: Number of y coordinates to be produced
    :param p: Parameter to be used
    :return: A list of y coordinates
    """

    y_coords = [initial_condition]

    # CREATE Y COORDINATES
    for i in range(steps):
        term = (p * y_coords[i]) * (1 - y_coords[i])
        y_coords.append(term)

    return y_coords

# MAIN PROGRAM
if __name__ == "__main__":

    list_of_p = [3.0, 3.4, 3.6785, 3.84, 4]

    # PLOT LOGISTIC MAPS
    for i in list_of_p:
        random_y = uniform(0, 1)
        print("LOGISTIC MAP PARAMETER", i, ":", logistic_map(random_y, 100, i))
        plt.plot(logistic_map(random_y, 100, i))
        plt.show()


