from random import random
from time import clock


def search(sequence, query):
    """
    Finds an item 'query' in a sorted list

    :param sequence: Sorted list
    :param query: Item being searched for
    :return: The index of the item query in the list or the next biggest item
                if item could not be found
    """

    # INITIALISE POINTERS
    start_pointer = 0
    end_pointer = len(sequence) - 1

    # BINARY SEARCH
    while start_pointer <= end_pointer:

        midpoint = (start_pointer + end_pointer) // 2   # Find midpoint

        if query <= sequence[midpoint]:     # Update pointers respectively
            end_pointer = midpoint - 1
        else:
            start_pointer = midpoint + 1

    return start_pointer


def make_random_seq(dim):
    """
    Makes a random sequence of size 'dim'

    :param dim: Size of generated sequence
    :return: List containing a random sequence
    """

    random_list = []

    for i in range(dim):
        random_list.append(int(random()*101))   # *101 to get values [0,100]

    return random_list


def insertion(sequence):
    """
    Build a new list from sequence inserting each item in the correct place

    :param sequence: Unsorted list
    :return: Sorted list
    """

    sorted_list = []

    for item in sequence:

        index = search(sorted_list, item)   # Find where to insert
        sorted_list.insert(index, item)     # Then insert

    return sorted_list


def sort_unique(sequence):
    """
    Constructs a list containing only one copy of each element in order

    :param sequence: Unsorted list, potentially containing multiple copies of
            one element
    :return: List containing one copy of each element in order
    """

    sorted_list = insertion(sequence)

    unique = []

    for item in sorted_list:

        if item in unique:      # If in list, skip
            continue
        else:
            unique.append(item)

    return unique


def unique(sequence):
    """
    Constructs a list from sequence that contains one copy of each element
        in order

    :param sequence: A list of elements
    :return: A sorted list, containing one copy of each element
    """

    sorted_list = []

    for item in sequence:

        point_to_insert = search(sorted_list, item)  # Find where to insert

        if point_to_insert > len(sorted_list) - 1:   # Insert at end of list
            sorted_list.append(item)

        elif sorted_list[point_to_insert] != item:   # Insert at 'index'
            sorted_list.insert(point_to_insert, item)

    return sorted_list


def run_time(func, *args):
    """
    Calculate the run time of a function

    :param func: function to be tested
    :param args: arguments to be passed to function
    :return: runtime of the function in seconds
    """
    start = clock()

    # RUN GIVEN FUNCTION
    func(*args)

    end = clock()

    return end-start


def test_func():
    """
    Function to compare run time of functions unique() and sort_unique() on
        randomly generated sequences of increasing size
    """

    for i in range(int(1e4), int(2.1e5), int(2e4)):

        # CREATE SEQUENCE
        sequence = make_random_seq(i)

        # CALCULATE TIMES AND RATIO
        u_time = round(run_time(unique, sequence), 3)
        su_time = round(run_time(sort_unique, sequence), 3)
        ratio = round(su_time / u_time, 2)

        # PRINT RESULTS
        print(' ' * (6 - len(str(i))), i, 'u:', u_time, end="")
        print(' ' * (6 - len(str(u_time))), 'su:', su_time, end="")
        print(' ' * (6 - len(str(su_time))), 'ratio:', ratio)


if __name__ == "__main__":

    # MAIN PROGRAM
    test_func()


