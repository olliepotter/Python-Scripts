import os

def visit(dname):
    """
    Recursively traverse the filesystem
    :param dname: Directory name
    :param pass_test_func: Test
    :return:
    """

    directories = os.listdir(dname)
    files = []

    for f in directories:

        path = os.path.join(dname, f)

        try:

            if os.path.isfile(path):
                    files.append(path)
            else:
                files = files + visit(path)

        except PermissionError:
            print("Permission Error Occurred")
            continue

    return files

print(os.listdir("C:/"))

list = visit("C:/")
for item in list:
    print(item)