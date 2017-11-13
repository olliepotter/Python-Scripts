from math import *
from Coursework_2.logisticmap import logistic_map
from random import uniform

def get_series(n, stype = 0):
    """
    Produces either a monotonic(0), alternating(1) or sinusoid(2) of length 'n'
    :param n: Length of the series
    :param stype: Type of the series
    :return: The series of length n
    """

    series = []

    for i in range(n):      # Loop through amount of times specified
        if stype == 0:      # Create monotonic series
            series.append(i)

        elif stype == 1:    # Create alternating series
            if i % 2 == 0:
                series.append(1)
            else:
                series.append(0)

        elif stype == 2:    # Create sinusoid series
            term = sin((2*pi)*500*(i/10000))    # Both 'sin' and 'pi' used from 'math' library
            series.append(term)

    return series


def horizontal_visibility_graph(series, weighted = False):
    """
    Take a series and works out the adjacency of the terms, then returning an adjacency matrix
    :param series: A series of numbers
    :param weighted: Whether the function should produce a weighted matrix or not
    :return: An adjacency matrix
    """

    # Build Matrix full of 0's
    size_of_each_row = len(series)
    amount_of_lists = len(series)
    matrix = [[0 for j in range(size_of_each_row)] for i in range(amount_of_lists)]

    if weighted:

        # Populate Matrix
        for i in range(len(series)):
            for j in range(len(series)):

                # Use custom functions to find values for comparison
                items_between = find_items_between(i, j, series)
                highest_between = highest_value_in_list(items_between)
                comparator = get_comparator(i, j, series)

                if i == j:
                    matrix[i][j] = 0
                elif i == (j + 1):
                    matrix[i][j] = round(1/(sqrt(((i-j)**2)+(series[i]-series[j])**2)), 3)
                elif i == (j - 1):
                    matrix[i][j] = round(1/(sqrt(((i-j)**2)+(series[i]-series[j])**2)), 3)
                elif highest_between < comparator:
                    matrix[i][j] = round(1/(sqrt(((i-j)**2)+(series[i]-series[j])**2)), 3)
                else:
                    matrix[i][j] = 0

    else:

        # Populate Matrix
        for i in range(len(series)):
            for j in range(len(series)):

                # Use custom functions to find values for comparison
                items_between = find_items_between(i, j, series)
                highest_between = highest_value_in_list(items_between)
                comparator = get_comparator(i, j, series)

                # Set values accordingly
                if i == j:
                    matrix[i][j] = 0
                elif i == (j + 1):
                    matrix[i][j] = 1
                elif i == (j - 1):
                    matrix[i][j] = 1
                elif highest_between < comparator:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0

    return matrix


def find_items_between(start_index, end_index, series):
    """
    Returns a list of everything between a specified
    start and end point in a list
    :param start_index: The starting index that specifies where in the list
    to take the data from
    :param end_index: The ending index that specifies where in the list
    to take the data from
    :param series: The list of terms
    :return: A list of all items between the two indexes specified
    """

    # To swap indexes over if starting > ending
    temp = end_index
    if start_index> end_index:
        end_index = start_index
        start_index = temp

    # Find all values in middle
    items_between = []
    for i in range(len(series)):

        if i == start_index:
            continue
        elif i == end_index:
            continue
        elif start_index <= i <= end_index:
            items_between.append(series[i])

    return items_between


def highest_value_in_list(series):
    # Find highest in-between
    greatest = 0
    for n in series:
        if n >= greatest:
            greatest = n

    return greatest


def get_comparator(index_1, index_2, series):
    """
    Finds the lowest item between two values at given indexes in a list and returns lowest
    :param index_1: First index point to compare the value of
    :param index_2: Second index point to compare the value of
    :param series: The list of values
    :return: The lowest of the two values at the specified indexes
    """

    # Find the values at the indexes so they can be compared
    value_1 = series[index_1]
    value_2 = series[index_2]
    comparator = 0

    # Take the lowest value of those two for comparison
    if value_1 >= value_2:
        comparator = value_2
    elif value_1 <= value_2:
        comparator = value_1

    return comparator


def print_hvg(hvg):

    # Loop through the list replacing 0's with spaces
    for i in range(len(hvg)):
        for j in range(len(hvg[i])):
            if hvg[i][j] == 0:
                hvg[i][j] = " "

    # Loop through list printing every item with space between for readability
    for i in range(len(hvg)):
        for j in range(len(hvg)):
            print(hvg[i][j], end="")
        print("")


def process_logisticmap(params, steps = 100):

    dictionary = {}

    for i in params:
        hvg = horizontal_visibility_graph(logistic_map(uniform(0, 1), p=i))
        dictionary[i] = hvg


    return dictionary


# Main Program
if __name__ == "__main__":

    # TESTER
    # list_of_numbers = [0.7, 0.525, 0.550, 0.9, 0.5, 0.75, 0.2, 0.6, 0.72, 0.3]
    # list_of_numbers = [1, 3, 2, 4, 6]
    # print_hvg(horizontal_visibility_graph(list_of_numbers, True))

    # CALCULATE SERIES
    monotonic = get_series(10, 0)
    alternating = get_series(10, 1)
    sinusoid = get_series(10, 2)

    # SERIES PRINTS
    print(monotonic)
    print(alternating)
    print(sinusoid)

    # PRINT ADJACENCY MATRICES
    print_hvg(horizontal_visibility_graph(monotonic))
    print_hvg(horizontal_visibility_graph(alternating, True))
    print_hvg(horizontal_visibility_graph(sinusoid))

    # LOGISTIC MAPPINGS
    logistic_parameters = [3.0, 3.4, 3.6785, 3.84, 4]
    logisticmap_dictionary = process_logisticmap(logistic_parameters)

    for key, value in logisticmap_dictionary.items():
        print("Key: ", key, ", Values: ", value)
        print_hvg(value)





