def choose_vertex(probability):
    """
    Randomly choose a vertex according
        to a given probability distribution.

    :param probability: Probability distribution
    :return: The chosen vertex identifier
    """

    import random

    # vertex identifiers
    vertex_ids = range(len(probability))

    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for vertex_id, vertex_probability in zip(vertex_ids, probability):
        cumulative_probability += vertex_probability
        # we have found the vertex to select
        if x < cumulative_probability:
            break

    return vertex_id
