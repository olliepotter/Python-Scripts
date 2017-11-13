import matplotlib.pyplot as plt
from random import *

list_of_p = [3.0, 3.4, 3.6785, 3.84, 4]


def logistic_map(initial_condition, steps=100, p=3.0):

    y_coords = [initial_condition]

    for i in range(steps):  # Iterate for given number of times, T
        term = (p * y_coords[i]) * (1 - y_coords[i])
        y_coords.append(term)

    return y_coords


if __name__ == "__main__":

    for i in list_of_p:
        random_y = uniform(0, 1)
        print(logistic_map(random_y, 100, i))
        plt.plot(logistic_map(random_y, 100, i))
        plt.show()


