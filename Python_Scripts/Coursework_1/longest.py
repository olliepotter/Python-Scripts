"""
This file contains functions read from a file and distinguish longest words within a file
"""

from reverse import print_reverse

filename = "words.txt"  # Declared here so file can be changed easily


def longest(words):
    """
    Finds the first longest word in a list
    :param words: A list of words
    :return: The first longest word found
    """
    count = 0    # You set the count to 0
    for i in words:  # Go through the whole list
        if len(i) > count:  # Checking for the longest string
            count = len(i)
            word = i
    return word


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


def all_longest(words):
    """
    Finds all the longest words in a given list
    :param words: A list of words
    :return: A list of all the longest words in the given list
    """
    longest_words = []

    length = len(longest(read_words(filename)))  # Specify the length of the longest word in the file

    for i in words:     # Loop through picking out all the words in the list with this length
        if len(i) == length:
            longest_words.append(i)

    return longest_words


if __name__ == "__main__":      # Main part of the program

    longest_word = longest(read_words(filename))
    print("The first longest word in the file is ", longest_word, "and has ", len(longest_word), " letters")

    output_list = all_longest(read_words(filename))  # Format output nicely
    for i in range(len(output_list)):
        print(output_list[i])

    print_reverse(longest_word)  # Call imported function from reverse.py
