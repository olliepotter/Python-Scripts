import os
from operator import itemgetter


def visit(dname, pass_test_func, max_n_results, no_files_found=[], first_run = True):
    """
    Recursively traverses the filesystem appending file paths and sizes to a
        list, dependant on a given test function

    :param dname: Directory name
    :param pass_test_func: Test
    :param max_n_results: Max number of results to be returned
    :param no_files_found: Used to return max number of results
    :param first_run: Test if first run so no_files_found can be reset
    :return: A list of file paths that pass the test function
    """

    directories = os.listdir(dname)
    files = []

    # REFRESH COUNTER ON FIRST RUN
    if first_run:
        no_files_found = []

    # LOOP THROUGH ALL DIRECTORIES IN CURRENT DIRECTORY
    for f in directories:
        try:

                path = os.path.join(dname, f)

                # BASE CASE - IF FILE THEN STOP
                if os.path.isfile(path):
                    if len(no_files_found) < max_n_results:
                        if pass_test_func(path):
                            files.append([path, os.path.getsize(path)])
                            no_files_found += [0]
                    else:
                        return files

                # RECURSIVE CASE - IF DIRECTORY CONTINUE RECURSION
                elif os.path.isdir(path):
                    files = files + visit(path, pass_test_func, max_n_results, no_files_found, False)

        # IGNORE PROTECTED FILES FROM OS
        except PermissionError:
            continue

        # IGNORE TEMPORARY FILES
        except FileNotFoundError:
            continue

    return files






def find_larger(path, max_n_results=10):
    """
    Recursively traverses from a given directory and prints file paths of files
        with suffix .txt and that are greater than 100,000 bytes

    :param path: Directory to begin traversing through
    :param max_n_results: Max number of results to be returned
    :return:
    """

    # GET FILE PATHS
    paths = visit(path, lambda file: True if os.path.getsize(file) > 100000 and file.endswith(".txt") else False, max_n_results)

    # CREATE DICTIONARY
    dictionary = create_sorted_dictionary(paths, True)

    # PRINT
    print("Finding .txt files with size larger than 100000 bytes")
    print_dictionary(dictionary)


def find_smaller(path, max_n_results=10):
    """
    Recursively traverses from a given directory and prints file paths of files
        with suffix .txt and that are smaller than 100 bytes

    :param path: Directory to begin traversing through
    :param max_n_results: Max number of results to be returned
    """

    # GET FILE PATHS
    paths = visit(path, lambda file: True if os.path.getsize(file) < 100 and file.endswith(".txt") else False, max_n_results)

    # CREATE DICTIONARY
    dictionary_of_files = create_sorted_dictionary(paths, False)

    # PRINT
    print("Finding .txt files with size smaller than 100 bytes")
    print_dictionary(dictionary_of_files)


def find_type(path, max_n_results=10):
    """
    Recursively traverses from a given directory and prints files paths of files
        with suffix .txt in descending order of file size

    :param path: Directory to begin traversing through
    :param max_n_results: Max number of results to be returned
    """

    # GET FILE PATHS
    paths = visit(path, lambda file: True if file.endswith(".txt") else False, max_n_results)

    # CREATE DICTIONARY
    dictionary_of_files = create_sorted_dictionary(paths, True)

    # PRINT
    print("Finding .txt files")
    print_dictionary(dictionary_of_files)


def print_dictionary(dictionary):
    """
    Formats the print of a given dictionary

    :param dictionary: dictionary of terms
    """

    for path, size in dictionary.items():   # List through all items
        print(' ' * (8 - len(str(size))), size, ' ' * 4, path)


def create_sorted_dictionary(paths, ascending):
    """
    Creates a dictionary sorted in ascending/descending order of file size

    :param paths: List of file paths
    :param ascending: Whether to print in ascending order of file size
    :return: Sorted dictionary
    """

    paths.sort(key=itemgetter(1), reverse=ascending)     # Sort list
    return {path: size for (path, size) in paths}     # Create Dictionary


if __name__ == "__main__":

    # FIND .TXT FILES ON C:/ DRIVE
    find_larger("C:/")
    find_smaller("C:/")
    find_type("C:/")
