a_matrix = [[0,0,1,0,1],[0,0,1,0,1],[1,1,0,0,0],[0,0,0,0,1],[1,1,0,1,0]]


eq = (a_matrix[0][0]*2**5) + (0*2**5) + (1*2**5) + (0*2**5) + (1*2**5)

eq1 = (0*2**5) + (0*2**5) + (1*2**5) + (0*2**5) + (1*2**5)

eq2 = (1*2**5) + (1*2**5) + (0*2**5) + (0*2**5) + (0*2**5)

eq3 = (0*1**5) + (0*1**5) + (0*1**5) + (0*1**5) + (1*1**5)

eq4 = (1*3**5) + (1*3**5) + (0*3**5) + (1*3**5) + (0*3**5)

print(eq)
print(eq1)
print(eq2)
print(eq3)
print(eq4)

if biased:

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):

            denominator_list = []
            denominator = 0
            a_ij = adj_matrix[i][j]
            d_alpha = count_edges(adj_matrix, j) ** alpha
            numerator = a_ij * d_alpha

            for k in range(len(adj_matrix)):
                a_ik = adj_matrix[i][k]
                d_j = count_edges(adj_matrix, k)
                denominator_list.append(a_ik * d_j ** alpha)
                denominator = denominator + (a_ik * d_j ** alpha)

                print("DENOMINATOR", denominator)
                print("DENOMINATOR_LIST", denominator_list)
                print("DENOMINATOR_SUM", sum(denominator_list))

                if denominator == 0:
                    continue
                else:
                    t_matrix[i][j] = numerator / denominator