rhyme = ['Mary', 'had', 'a', 'little', 'lamb', 'whose', 'fleece', 'was', 'white', 'as', 'snow']
letters = 0
words = 0

def wlcount(list):
    letters = 0
    words = 0

    for i in list:
        letters += len(i)
        words += 1

    return letters, words


print(wlcount(rhyme))
