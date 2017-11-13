sequence = [0]

def fibonacci(number, next_value=1, prev_value=0):

    if number == 0:
        return prev_value
    if number == 1:
        return next_value

    sequence.append(next_value)

    return fibonacci(number - 1, next_value + prev_value, next_value)


def makeFib(n):

    myList = []

    for count in range(n):
        if count < 2:
            myList.append(count)
        else:
            myList.append(myList[count-1] + myList[count-2])

    print(myList)


def fib(n):
    F = []

    for i in range(n):

        if len(F) == 0:
            F.append(0)

        elif len(F) == 1:
            F.append(1)

        else:
            F.append(F[i - 1] + F[i - 2])

    return F


def auxfib(n):
    F = []

    for i in range(n):

        if len(F) == 0:
            F.append(0)

        elif len(F) == 1:
            F.append(1)

        else:
            F.append(F[i - 1] + F[i - 2])

    last_two_numbers = [F[-1], F[-2]]

    return last_two_numbers


print(fib(20))


def fibonacci(number, next_value=1, prev_value=0):

    if number == 0:
        return prev_value
    if number == 1:
        return next_value

    return fibonacci(number - 1, next_value + prev_value, next_value)

def fibonacci(number):

    if number == 0:
        return number
    if number == 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


def auxfib(number):
    if number == 0:
        return 0, 0

    num1 = fibonacci(number)
    num2 = fibonacci(number-1)
    return num1, num2