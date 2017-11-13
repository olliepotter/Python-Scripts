rhyme = ['Mary', 'had', 'a', 'little', 'lamb', 'whose', 'fleece', 'was', 'white', 'as', 'snow']
letters = 0
words = 0

for i in rhyme:
    letters += len(i)
    words += 1


print(letters)
print(words)
