from Coursework_3.choose import run_time
from random import random


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

    # INITIAL CHECKS
    if len(sequence) == 0:
        return 0
    elif query > sequence[-1]:
        return len(sequence)

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
        random_list.append(int(random()*101))

    return random_list


def insertion(sequence):
    """
    Build a new list from sequence inserting each item in the correct place

    :param sequence: Unsorted list
    :return: Sorted list
    """

    sorted_list = []

    # LOOP THROUGH ALL TERMS
    for item in sequence:

        # FIND WHERE TO INSERT THEN INSERT
        index = search(sorted_list, item)
        sorted_list.insert(index, item)

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

        if item in unique:
            continue
        else:
            unique.append(item)

    return unique


def unique(sequence):

    sorted_list = []

    for item in sequence:

        # FIND WHERE TO INSERT THE ITEM
        point_to_insert = search(sorted_list, item)

        # ITEM TO BE INSERTED AT END OF LIST
        if point_to_insert > len(sorted_list) - 1:
            sorted_list.append(item)

        # INSERT INTO LIST
        elif sorted_list[point_to_insert] != item:
            sorted_list.insert(point_to_insert, item)

    return sorted_list


def test_func():

    for i in range(int(1e4), int(2.1e5), int(2e4)):
        sequence = make_random_seq(i)
        u_time = run_time(unique, sequence)
        su_time = run_time(sort_unique, sequence)

        print(i, "u: ", u_time, end=" ")
        print("su: ", su_time, end=" ")
        print("ratio: ", su_time/u_time)


if __name__ == "__main__":

    test_func()
    # list = [1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 6]
    # print(search(list, 5))


