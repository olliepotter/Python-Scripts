from Workshop_4.powers import sum_powers

def odd(L):
    list_of_odd = []
    for i in range(len(L)):
        if (L[i] % 2) != 0:
            list_of_odd.append(L[i])

    return list_of_odd


def odd_even(L):
    list_of_odd = []
    list_of_even = []

    for i in range(len(L)):
        if (L[i] % 2) == 0:
            list_of_even.append(L[i])
        else:
            list_of_odd.append(L[i])

    return list_of_odd, list_of_even


def squeeze(L):
    new_list = []
    for i in range(len(L)):
        if L[i] in new_list:
            continue
        else:
            new_list.append(L[i])

    return new_list


print(odd(list(range(20))))
print(odd_even(list(range(20))))
print(sum_powers(odd_even(list(range(20)))[0], 2))
print(sum_powers(odd_even(list(range(20)))[1], 2))

my_list = [0, 1, 2, 2, 3, 2]
print(squeeze(my_list))
