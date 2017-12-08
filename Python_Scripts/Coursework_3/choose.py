from time import clock


def sierpinski_triangle(dim, choose_func, display):
    """
    Creates the Sierpinski Triangle of a given size

    :param dim: Size of the triangle
    :param choose_func: Function to compute binomial coefficient
    :param display: Whether the function prints or not
    :return: The Sierpinski Triangle of the given size
    """

    # CHECK POSITIVE INTEGER
    assert dim >= 0 and type(dim) == int

    triangle = []

    # BUILD SIERPINSKI TRIANGLE
    for i in range(dim):

        row = ["*"]     # Start each row with 1, I.E *

        for j in range(i):

            term = choose_func(i, j + 1)

            if term % 2 == 1:       # Adding * to row whenever odd
                row.append("*")
            else:
                row.append(" ")

        triangle.append(row)    # Add row to triangle

    if display:

        # LOOP THROUGH ALL VALUES IN TRIANGLE
        for i in range(len(triangle)):
            for j in range(i+1):

                # PRINT ADDING NEW LINES WHEN NEEDED
                if i == j:
                    print(triangle[i][j])
                else:
                    print(triangle[i][j], end=" ")

    return triangle











def run_time(func, *args):
    """
    Calculate the run time of a function

    :param func: function to be tested
    :param args: arguments to be passed to function
    :return: runtime of the function in seconds
    """

    start = clock()

    func(*args)

    end = clock()

    return round(end-start, 8)


def choose_simple(n, k):
    """
    Computes the value of ”n choose k”

    :param n: Amount to choose from
    :param k: Amount to be chosen
    :return: Value of "n choose k"
    """

    # VALIDATE INPUT
    assert type(n) == int and type(k) == int, "n and k must be integers"
    assert k <= n, "k can not be greater than n"
    assert n >= 0 and k >= 0, "n and k must both be positive"

    # BASE CASE
    if k == 0 or k == n:
        return 1

    # RECURSIVE CASE
    else:
        return choose_simple(n - 1, k - 1) + choose_simple(n - 1, k)


def choose_mem(n, k):
    """
    Computes the value of ”n choose k” using memoization

    :param n: Amount to choose from
    :param k: Amount to be chosen
    :return: Value of "n choose k"
    """

    # VALIDATE INPUT
    assert type(n) == int and type(k) == int, "n and k must be integers"
    assert k <= n, "k can not be greater than n"
    assert n >= 0 and k >= 0, "n and k must both be positive"

    # CHECK CACHE
    if (n, k) in __choose_cache:
        return __choose_cache[n, k]

    # BASE CASE
    if k == 0 or k == n:
        return 1

    # RECURSIVE CASE
    else:
        choose_value = choose_mem(n - 1, k - 1) + choose_mem(n - 1, k)
        __choose_cache[n, k] = choose_value
        return choose_value


    
def test_choose_mem(triangle_size):
    """
    Computes and prints the runtime of the function sierpinski_triangle using
        the choose_mem function for increasing values up to triangle_size

    :param triangle_size: The size of the triangle sierpinski triangle computes
    """

    for i in range(1, triangle_size + 1):

        # IF LESS THAN 10 PRINT WITH 4 SPACES FOR NICE PRINTING
        if i < 10:
            print(i, "    ",
                  run_time(sierpinski_triangle, i, choose_mem, False))

        # ELSE PRINT WITH 3 SPACES
        else:
            print(i, "   ",
                  run_time(sierpinski_triangle, i, choose_mem, False))


def test_choose_simple(triangle_size):
    """
    Computes and prints the runtime of the function sierpinski_triangle using
        the choose_simple function for increasing values up to triangle_size

    :param triangle_size: The size of the triangle sierpinski triangle computes
    """

    for i in range(1, triangle_size + 1):

        # IF LESS THAN 10 PRINT WITH 4 SPACES FOR NICE PRINTING
        if i < 10:
            print(i, "    ", run_time(sierpinski_triangle, i, choose_simple, False))

        # ELSE PRINT WITH 3 SPACES
        else:
            print(i, "   ", run_time(sierpinski_triangle, i, choose_simple, False))


if __name__ == "__main__":

    # INITIALISE CACHE FOR CHOOSE_MEM
    __choose_cache = {}

    # PRINT TRIANGLE
    sierpinski_triangle(16, choose_mem, True)
    print()

    # PRINT CHOOSE_MEM
    print("test_choose_mem(16)")
    test_choose_mem(16)
    print()

    # PRINT CHOOSE_SIMPLE
    print("test_choose_simple(16)")
    test_choose_simple(16)
