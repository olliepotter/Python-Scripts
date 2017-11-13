def sum_powers(L, p=1):
    sum = 0
    for n in range(len(L)):
        sum = sum + (L[n])**p

    return sum


for i in range(10):
    print(sum_powers(list(range(10)), i))
