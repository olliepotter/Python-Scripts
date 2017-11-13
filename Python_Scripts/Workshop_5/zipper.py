def zipper(a, b):
    output_list = []
    if len(a) == len(b):
        for i in range(len(a)):
            new_list = []
            new_list.append(a[i])
            new_list.append(b[i])
            output_list.append(new_list)

        return output_list
    else:
        return "Invalid! Lists do not have the same number of arguments."


if __name__ == "__main__":

    a = [3, 4, 5, 6]
    b = ['a', 'b', 'c', 'd']

    print(zipper(a, b))
