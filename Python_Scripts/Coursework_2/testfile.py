def find_greatest_p(i, j, list_of_terms):
    """
    Finds the greatest value between the first and last item of the list
    :param list_of_terms: A list of terms
    :return: The greatest item between the first and last term of the list
    """
    start_point = list_of_terms[0]
    end_point = list_of_terms[len(list_of_terms)-1]
    comparator = 0

    # Take the lowest value of those two for comparison
    if start_point >= end_point:
        comparator = end_point
    elif start_point <= end_point:
        comparator = start_point

    # Find all values in middle
    items_between = []
    for i in list_of_terms:
        if i == start_point:
            continue
        elif i == end_point:
            continue
        else:
            items_between.append(i)

    # Find highest in-between
    greatest = 0
    for i in items_between:
        if i >= greatest:
            greatest = i

    # If greatest <= comparator then set to 1
    if greatest <= comparator:
        return 1
    else:
        return 0



    # Print diagnostics
    print(items_between)
    print(start_index, "", start_value)
    print(end_index, "", end_value)
    print("Comparator: ", comparator)
    print("Greatest: ", greatest)

    # If greatest <= comparator then set to 1
    if greatest <= comparator:
        return 1
    else:
        return 0




        else:
            # if i < j:
                # then swap
            if set[i] and set[j] >= find_greatest_p(i, j, set):
                Matrix[i][j] = 1



# If greatest <= comparator then set to 1
                # if greatest <= comparator:
                #    Matrix[i][j] = 1
                # else:
                #    Matrix[i][j] = 0