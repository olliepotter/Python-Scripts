"""
This file contains various functions for operations involving the golden ratio
"""

from fibonacci import *     # Import fibonacci functions for use later


def golden_ratio_sequence(n):
    """
    Returns a list of size 'n', golden ratio values using incremental fibonacci numbers
    :param n: To count the amount of terms that should be returned
    :return list_of_ratios: A list containing all of the golden ratios
    """
    list_of_ratios = []     # Initialise so each time function is called we have an empty list

    for i in range(n):      # Loop through each fibonacci number
        if i == 0:
            list_of_ratios.append(0.0)      # Fibonacci(0) = 0 so avoid "Divide by zero" error
        elif i == 1:
            list_of_ratios.append(1.0)      # Fibonacci(1) = 1 to avoid extra function call
        elif i > 1:
            list_of_ratios.append(fibonacci(i+1)/fibonacci(i))  # Divide next number by current number in sequence

    return list_of_ratios


def find_golden_ratio(n):
    """
    Finds the value of the golden ratio at point 'n' into the fibonacci sequence
    :param n: Used to distinguish which numbers in the fibonacci sequence are used
    :return: A golden ratio value
    """

    if n == 0:
        return 0.0      # When looking for the 0th term just return 0

    return fibonacci(n+1) / fibonacci(n)    # Formula for golden ratio


def find_minimum_fibonacci_numbers(tolerance=0.0000000001, maxnum=100):
    """
    A function that finds the amount of numbers in the fibonacci sequence that are required to converge on a constant
    value of the golden ratio to a given tolerance

    :param tolerance: The degree of accuracy as to which the golden ratio is found
    :param maxnum: The maximum number of fibonacci numbers to be used to find the golden ratio
    :return: The only time return is used, is to stop the function should the maxnum be exceeded
    """
    gr = 1.6180339887498948                                # Golden ratio constant
    n = 0

    while abs(find_golden_ratio(n) - gr) > tolerance:      # Loop until accuracy of the tolerance is met
        n = n + 1                                          # Count the amount of fibonacci numbers used
        num_fibonacci_terms = n + 2  # Account for 0, 1 at the start of the fibonacci sequence to avoid div by 0 error

        if num_fibonacci_terms >= maxnum:  # Check if the amount of fibonacci numbers used exceeds max

            print("The number of fibonacci numbers used: ", num_fibonacci_terms, "\n",     # Format output nicely
                  "CALCULATED GOLDEN RATIO:    ", find_golden_ratio(n), "\n",
                  "ACTUAL GOLDEN RATIO:        ", gr, "\n",
                  "Max number of fibonacci terms reached\n")
            return

    print("The number of fibonacci numbers used: ", num_fibonacci_terms, "\n",             # Format output nicely
          "CALCULATED GOLDEN RATIO:    ", find_golden_ratio(n), "\n",
          "ACTUAL GOLDEN RATIO:        ", gr, "\n")                        # Print constant for easy comparison


if __name__ == "__main__":

    sequence = golden_ratio_sequence(20)  # Format output nicely

    for i in range(len(sequence)):
        print(sequence[i])

    find_minimum_fibonacci_numbers()
    find_minimum_fibonacci_numbers(10**-14)
    find_minimum_fibonacci_numbers(10**-18)
