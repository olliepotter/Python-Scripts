from fibonacci import fib

def goldenratio_sequence(n):

    list_of_ratios = []
    list_of_fib = fib(n+1)

    for i in range(n):
        if i == 0 | i == 1:
            list_of_fib.append(0)
        else:
            list_of_ratios.append(list_of_fib[(i)]/list_of_fib[(i-1)])

    return list_of_ratios


def find_golden_ratio(n):
    if n == 0:
        return 0.0
    elif n == 1:
        return 1.0

    fiblist = auxfib(n)
    number1 = fiblist[0]
    number2 = fiblist[1]
    return number1 / number2


def goldenratio_sequence(n):

    list_of_ratios = []
    list_of_fib = fib(n+1)

    for i in range(n):
        if i == 0 | i == 1:
            list_of_ratios.append(0.0)
        elif i > 1:
            list_of_ratios.append(list_of_fib[(i)]/list_of_fib[(i-1)])

    return list_of_ratios


altgolden

#while(round(find_golden_ratio(n), 10) != round(gr, 10)):
    #    print("OUR GOLDEN RATIO: ", round(find_golden_ratio(n), 10))
    #    print("GR:               ", round(gr, 10))
    #    n += 1

    #if (round(find_golden_ratio(n), 10) == round(gr, 10)):
    #    print("SPC OUR GOLDEN RATIO: ", round(find_golden_ratio(n), 10))
    #    print("SPC GR:               ", round(gr, 10))