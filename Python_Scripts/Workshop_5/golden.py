from math import sqrt


def golden(N):

    output_list = [1]

    for i in range(N):
        if i == 1:
            continue
        else:
            output_list.append(sqrt(1 + output_list[i-1]))

    return output_list


print(golden(20))
