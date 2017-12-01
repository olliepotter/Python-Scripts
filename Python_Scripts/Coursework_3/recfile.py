import os
from Coursework_3 import choose
from operator import itemgetter


def visit(dname, pass_test_func, max_n_results=100):
    """
    Recursively traverses the filesystem appending file paths and sizes to a
        list, dependant on a given test function

    :param dname: Directory name
    :param pass_test_func: Test
    :param max_n_results: Max number of results to be returned
    :return:
    """

    directories = os.listdir(dname)
    files = []
    global counter

    # LOOP THROUGH ALL DIRECTORIES IN CURRENT DIRECTORY
    for f in directories:
        try:

                path = os.path.join(dname, f)

                # BASE CASE - IF FILE THEN STOP
                if os.path.isfile(path):
                    if counter < max_n_results:
                        if pass_test_func(path):
                            files.append([path, os.path.getsize(path)])
                            counter += 1
                    else:
                        return files

                # RECURSIVE CASE - IF DIRECTORY CONTINUE RECURSION
                elif os.path.isdir(path):
                    files = files + visit(path, pass_test_func, max_n_results)

        # DEAL WITH PROTECTED FILES FROM OS
        except PermissionError:
            continue

        # DEAL WITH TEMPORARY FILES
        except FileNotFoundError:
            continue

    return files


def find_larger(path, max_n_results=10):
    """
    Recursively traverses from a given directory and prints file paths of files
        with suffix .txt and that are greater than 100,000 bytes

    :param path: The directory to begin traversing through
    :param max_n_results:
    :return:
    """

    # GET FILE PATHS
    paths = visit(path, lambda file: True if os.path.getsize(file) > 100000 and file.endswith(".txt") else False, max_n_results)

    # SORT LIST
    paths.sort(key=itemgetter(1), reverse=True)

    # CREATE DICTIONARY
    dictionary = {path: size for (path, size) in paths}

    # FORMAT PRINT
    print("Finding .txt files with size larger than 100000 bytes")
    print_dictionary(dictionary)


def find_smaller(path, max_n_results=10):
    """
    Recursively traverses from a given directory and prints file paths of files
        with suffix .txt and that are smaller than 100 bytes

    :param path: The directory to begin traversing through
    :param max_n_results:
    :return:
    """

    # GET FILE PATHS
    paths = visit(path, lambda file: True if os.path.getsize(file) < 100 and file.endswith(".txt") else False, max_n_results)

    # SORT LIST
    paths.sort(key=itemgetter(1), reverse=False)

    # CREATE DICTIONARY
    dictionary = {path: size for (path, size) in paths}

    # FORMAT PRINT
    print("Finding .txt files with size smaller than 100 bytes")
    print_dictionary(dictionary)


def find_type(path, max_n_results=10):

    # GET FILE PATHS
    paths = visit(path, lambda file: True if file.endswith(".txt") else False, max_n_results)

    # SORT LIST
    paths.sort(key=itemgetter(1), reverse=True)

    # CREATE DICTIONARY
    dictionary = {path: size for (path, size) in paths}

    # FORMAT PRINT
    print("Finding .txt files")
    print_dictionary(dictionary)


def print_dictionary(dictionary):

    for path, size in dictionary.items():
        print("    ", size, "    ", path)


def print_list(any_list):
    """
    Prints all items in a list

    :param any_list: a list
    :param max_n_items: Max number of values to be printed
    :return:
    """

    for item in any_list:
        print(item)


counter = 0
print(choose.run_time(find_type, "C:/"))
print()
# find_smaller("..\Coursework_3")






