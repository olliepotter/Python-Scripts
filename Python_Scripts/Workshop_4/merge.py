def merge(A, B):
    final_list = []

    length = len(A) + len(B)

    for i in range(length):
        if len(A) == 0:
            final_list.append(B[0])
            B.pop(0)
        elif len(B) == 0:
            final_list.append(A[0])
            A.pop(0)
        elif A[0] < B[0]:
            final_list.append(A[0])
            A.pop(0)
        elif B[0] < A[0]:
            final_list.append(B[0])
            B.pop(0)

    return final_list


A = [1, 5, 6, 7]
B = [2, 3, 8, 9, 10]

print(merge(A, B))