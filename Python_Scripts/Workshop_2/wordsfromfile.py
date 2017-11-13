file = open('../words.txt', 'r')
lines = file.readlines()
chars = 0
words = 0

for i in lines:
    chars += len(i.strip())
    words += 1

average_length = chars / words

print(chars)
print(average_length)