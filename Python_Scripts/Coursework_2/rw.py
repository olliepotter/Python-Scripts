from Coursework_2.logisticmap import logistic_map
from Coursework_2.HVG import *
from Coursework_2.choose_vertex import choose_vertex

def get_graph_from_series(length=25):
    series = logistic_map(0.1, length, 4)
    matrix = horizontal_visibility_graph(series)
    return matrix


def random_walk(adj_matrix, steps=1000, biased=False, alpha=1.0):

    visited_vertices = []

    if biased:

        transition_matrix = create_transition_matrix(adj_matrix, True, 5)

        initial_vertex_distribution = find_initial_vertices(adj_matrix, True, 5)

        visited_vertices.append(choose_vertex(initial_vertex_distribution))
        for i in range(1, steps):
            prev = visited_vertices[len(visited_vertices) - 1]
            visited_vertices.append(choose_vertex(transition_matrix[prev]))

        return visited_vertices


    else:
        transition_matrix = create_transition_matrix(adj_matrix)

        initial_vertex_distribution = find_initial_vertices(adj_matrix)

        visited_vertices.append(choose_vertex(initial_vertex_distribution))
        for i in range(1, steps):
            prev = visited_vertices[len(visited_vertices) - 1]
            visited_vertices.append(choose_vertex(transition_matrix[prev]))

    return visited_vertices


def create_transition_matrix(adj_matrix, biased=False, alpha=0):

    t_matrix = [[0 for j in range(len(adj_matrix))] for i in
              range(len(adj_matrix))]

    if biased:

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):

                denominator = 0
                a_ij = adj_matrix[i][j]
                d_alpha = count_edges(adj_matrix, j) ** alpha
                numerator = a_ij * d_alpha

                for k in range(len(adj_matrix)):
                    a_ik = adj_matrix[i][k]
                    d_j = count_edges(adj_matrix, k)
                    denominator = denominator + (a_ik * d_j ** alpha)

                    if denominator == 0:
                        continue
                    else:
                        t_matrix[i][j] = numerator / denominator

    else:

        for i in range(len(adj_matrix)):

            probability = 1/count_edges(adj_matrix, i)

            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] == 1:
                    t_matrix[i][j] = probability

    return t_matrix


def count_edges(adj_matrix, row_index):

    row = adj_matrix[row_index]
    count = 0

    for i in row:
        if i != 0:
            count += 1

    return count


def find_initial_vertices(adj_matrix, biased=False, alpha=0):

    total_ones = 0
    ones_in_row = []
    initial_vertices = []
    numerators = []

    if biased:

        for i in range(len(adj_matrix)):

            # C CALCULATION
            d_j_alpha = count_edges(adj_matrix, i) ** alpha

            # NUMERATOR CALCULATIONS
            c_i = count_edges(adj_matrix, i) * d_j_alpha
            d_i_alpha = count_edges(adj_matrix, i) ** alpha
            numerator = c_i * d_i_alpha
            numerators.append(numerator)

            # DENOMINATOR CALCULATION
            denominator = sum(numerators)

        for i in range(len(adj_matrix)):
            initial_vertices.append(numerators[i] / denominator)

        return initial_vertices

    else:

        # CALCULATE PROBABILITY
        for i in range(len(adj_matrix)):
            total_ones = total_ones + count_edges(adj_matrix, i)
            ones_in_row.append(count_edges(adj_matrix, i))

        for i in range(len(adj_matrix)):
            initial_vertices.append(ones_in_row[i]/total_ones)

    return initial_vertices


def print_triplets(visited_vertices, k=20):

    number_triplets_poss = len(visited_vertices) - 2
    print(visited_vertices)

    if number_triplets_poss >= k:
        for i in range(k):
            print(visited_vertices[i:i+3], end='')
    else:
        for i in range(number_triplets_poss):
            print(visited_vertices[i:i+3], end='')
        print("\nOnly", number_triplets_poss, "triplets were possible")


def verify_equality(adj_matrix):
    if create_transition_matrix(adj_matrix) == create_transition_matrix(adj_matrix, True, 0):
        print("True")
    else:
        print("False")


def histogram(adj_matrix):
    for i in range(len(adj_matrix)):
        print("Vertex ID", i, ":", "*"*count_edges(adj_matrix,i))


def count_vertex_occurrence(visited_verticies):

    dictionary = {}
    items_present = []

    # FIND ITEMS PRESENT
    for i in visited_verticies:
        if i not in items_present:
            items_present.append(i)

    items_present.sort()

    for i in items_present:
        dictionary[i] = visited_verticies.count(i)

    print(dictionary)
    for vertex, times_visited in dictionary.items():
        print("Vertex: ", vertex, ", Times Visited: ", times_visited)




get_graph_from_series()
list_of_numbers = [1, 3, 2, 4, 6]
a_matrix = [[0,0,1,0,1],[0,0,1,0,1],[1,1,0,0,0],[0,0,0,0,1],[1,1,0,1,0]]

print("ADJACENCY MATRIX:")
for i in a_matrix:
    print(i)

print("TRANSITION MATRIX:")

for i in create_transition_matrix(a_matrix):
    print(i)

print()

for i in create_transition_matrix(a_matrix, True, 0):
    print(i)

print()
print_triplets(random_walk(a_matrix, 200))
verify_equality(a_matrix)
histogram(a_matrix)
count_vertex_occurrence(random_walk(a_matrix, 200))
count_vertex_occurrence(random_walk(a_matrix, 200))
count_vertex_occurrence(random_walk(a_matrix, 200, True, 5))



# print("RANDOM WALK:")
# print(random_walk(a_matrix, 200))
# print(random_walk(a_matrix, 200, True, 5))




