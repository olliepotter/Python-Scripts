from Workshop_5.zipper import zipper


def dotv2(a, b):

    sum = 0

    if len(a) == len(b):
        for A, B in zipper(a, b):
            product = A * B
            sum = sum + product

        return sum
    else:
        return "Invalid! Lists do not have the same number of arguments."


a = [0.04904772, 1.38633599, 0.94084723, -0.96782833, -0.66058869]
b = [1.07227778, -0.75143678, 0.54550933, 0.20866252, -1.4619395]

print(dotv2(a, b))
