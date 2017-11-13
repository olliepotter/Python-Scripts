"""
Contains various functions that print a string in reverse order
"""


def print_reverse(text, print_spaces=False):
    """
    Print a string in reverse with each character on a new line
    :param text: The string to be reversed
    :param print_spaces: To distinguish whether a number of spaces should be printed in front of each character
           corresponding to their index position in the string
    """
    length_of_string = len(text)

    # Decide whether to print spaces or not
    if print_spaces:

        # Reverse the string adding spaces and new lines
        for i in range(length_of_string):
            if i == (length_of_string-1):
                print(text[-(i+1)])  # Start from the end of the string but +1 to account for index starting at 0
            else:
                print(" " * (length_of_string - (i+1)) + text[-(i+1)])  # +1 to account for index

    else:

        # Reverse the string with no spaces
        for i in range(length_of_string):
            print(text[-(i + 1)])


if __name__ == '__main__':  # Main part of the program

    print_reverse("reversestring")
    print_reverse("reversestring", True)
