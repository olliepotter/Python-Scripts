from time import clock


def sierpinski_triangle(dim, choose_func, display):
    """
    Creates the Sierpinski Triangle up to a given size

    :param dim: Size of the triangle
    :param choose_func: Function to compute binomial coefficient
    :param display: Whether the function prints or not
    :return: The Sierpinski Triangle of the given size
    """

    triangle = []

    # BUILD SIERPINSKI TRIANGLE
    for i in range(dim):

        # START EACH ROW WITH 1, I.E *
        row = ["*"]

        for j in range(i):

            term = choose_func(i, j + 1)

            # ADDING * TO ROW WHENEVER ODD
            if term % 2 == 1:
                row.append("*")
            else:
                row.append(" ")

        # ADD ROW TO TRIANGLE
        triangle.append(row)

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

    start = clock()

    # RUN GIVEN FUNCTION
    func(*args)

    end = clock()

    return round(end-start, 8)


def choose_simple(n, k):

    # VALIDATE INPUT
    assert k <= n, "k can not be greater than n "
    assert n >= 0, "n and k must both be positive"

    # BASE CASE
    if k == 0 or k == n:
        return 1

    # RECURSIVE CASE
    else:
        return choose_simple(n - 1, k - 1) + choose_simple(n - 1, k)


def choose_mem(n, k):

    # VALIDATE INPUT
    assert k <= n, "k can not be greater than n "
    assert n >= 0, "n and k must both be positive"

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

    __choose_cache = {}

    sierpinski_triangle(16, choose_mem, True)

    test_choose_mem(16)

    print()

    test_choose_simple(16)







