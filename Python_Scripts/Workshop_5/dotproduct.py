def dot(a, b):
    sum = 0
    if len(a) == len(b):
        for i in range(len(a)):
            product = a[i] * b[i]
            sum = sum + product
        return sum
    else:
        return "Invalid! Length of two lists are different."


a = [0.04904772, 1.38633599, 0.94084723, -0.96782833, -0.66058869]
b = [1.07227778, -0.75143678, 0.54550933, 0.20866252, -1.4619395]

print(dot(a, b))
