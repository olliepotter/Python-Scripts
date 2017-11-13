limerick = [
    ['There','was', 'a', 'young', 'lady', 'named', 'Wright'],
    ['Whose', 'speed', 'was', 'much', 'faster', 'than', 'light'],
    ['She', 'left', 'home', 'one', 'day'],
    ['In', 'a', 'relative', 'way'],
    ['And', 'returned', 'on', 'the', 'previous', 'night']
]


def nice_print(L):
    for lists in L:
        for i in range(len(lists)):
            if i == len(lists)-1:
                print(lists[i])
            else:
                print(lists[i], "", end='')


nice_print(limerick)
