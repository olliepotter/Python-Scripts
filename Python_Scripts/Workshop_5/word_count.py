def word_count(L):

    char_count = 0
    word_count = 0

    for words in L:
        word_count += 1
        for letters in words:
            char_count += 1

    return print(char_count, word_count)


rhyme = ['Mary', 'had', 'a', 'little', 'lamb', 'whose', 'fleece', 'was', 'white', 'as', 'snow']
word_count(rhyme)
