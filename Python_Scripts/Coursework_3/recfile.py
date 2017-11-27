import os

dirlist = os.listdir("../Coursework_1")


# for f in dirlist:
#     path = "../Coursework_1/" + f
#
#     if os.path.isfile(path):
#         print("TRUE")
#     else:
#         print("FALSE")
#
#     if os.path.isdir(path):
#         print(f, "IS A DIRECTORY")
#     else:
#         print(f, "IS NOT A DIRECTORY")



def visit(dname):
    """
    Recursively traverse the filesystem
    :param dname: Directory name
    :param pass_test_func: Test
    :return:
    """
    # FOR LOOP

    # BASE CASE
    # when content is a file
    if os.path.isfile(dname):
        print("TRUE, IS A FILE")
    else:
        print("FALSE, IS NOT A FILE")

    # RECURSIVE CASE
    # when content is a directory
    if os.path.isdir(dname):
        return visit(dname)


print(visit("../Coursework_1"))
# CREATE DICTIONARY OF PATH AND SIZE
# def visit(dname, pass_test_func):
    # Visit directory
    # Loop through all contents
    # If directory call visit on itself
#
#     return conforming_files[]
