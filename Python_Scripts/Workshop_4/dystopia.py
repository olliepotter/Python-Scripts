def read_words(filename):
    """
    Reads words from a file and returns them in a list stripped of line breaks and whitespace
    :param filename: Name of the file to be read
    :return: A list containing each word read from the given file
    """
    file = open(filename, 'r')  # Open the given file in 'read' mode
    words_from_file = file.read().splitlines()  # Strip line breaks
    file.close()

    return words_from_file

all_words = read_words("words.txt")
e_words = []

for i in all_words:
    if "a" in i or "A" in i:
        continue
    elif "i" in i or "I" in i:
        continue
    elif "o" in i or "I" in i:
        continue
    elif "u" in i or "U" in i:
        continue
    else:
        e_words.append(i)

print(len(e_words))

def find_vowel(vowel):
    for i in range(len(all_words)):  # Loop through all words
        for j in range(vowels): # Loop through all vowels checking if they are in word
            if vowels[j] in all_words[i] and vowels[j+1]: # If a vowel is in the word
                i.replace(vowel[j], '') # Remove vowel from the word
                i.replace(vowel[j+1], '')
                j = j + 1
                i = i -1









vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
single_vowel = []
# Loop through all the words
    # Checking if word has more than one of 'vowels'
        #skip
    #else
        #append

print(single_vowel)