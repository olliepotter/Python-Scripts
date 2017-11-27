def factorial(n):
    if n == 0:

        print("n = 0 returning 1\ n ")
        return 1

    else:

        print(" " * (n - 1), "n = ", n, end=" ")
        print("calling factorial ( ", n - 1, ")")
        input("?")  # Wait for user to press return
        f = n * factorial(n - 1)
        print(" " * (n - 1), "n = ", n, "returning", f)
        input("?")  # Wait again
        return f


f = factorial(5)
print("The result is ", f)
