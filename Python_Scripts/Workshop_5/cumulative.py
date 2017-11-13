def cumulative(numbers):
    output_list = []
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
        output_list.append(total)

    return output_list


numbers = [5, 10, 3, 8]

print(cumulative(numbers))