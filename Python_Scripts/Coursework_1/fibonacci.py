"""
This file contains various functions to compute a given number of fibonacci terms
"""


def fibonacci(number, next_value=1, prev_value=0):
    """
    Calculates the 'nth' number in the fibonacci sequence
    :param number: The 'nth' term in the fibonacci sequence to be returned
    :param next_value: The next value in the sequence
    :param prev_value: The previous value in the sequence
    :return: Decrement of the number, the new value calculated, the now previous value
    """

    if number == 0:
        return prev_value
    if number == 1:
        return next_value

    return fibonacci(number - 1, next_value + prev_value, next_value)  # Function is recursive


def fibonacci_sequence(n):
    """
    Returns a list containing each number in the fibonacci sequence up to 'n' terms
    :param n: The amount of items to be returned
    :return: A list of fibonacci numbers , size n
    """
    sequence = []

    for i in range(n):  # Loop through n times to make a list of size n populated with terms from fibonacci sequence
        sequence.append(fibonacci(i))

    return sequence


if __name__ == '__main__':  # Main part of the program

    output_list = fibonacci_sequence(20)

    for i in range(len(output_list)):    # Format output nicely
        print(output_list[i])
