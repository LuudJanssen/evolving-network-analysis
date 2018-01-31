import numpy
import numpy.random
import click
from graph_tool.topology import shortest_distance


# Gets the shortest paths mean
def shortest_paths_mean(graph):
    frequency_dict = {}

    # max path length equals the diameter 
    for i in range(100):
        frequency_dict[i] = 0

    vertices = graph.get_vertices()
    numpy.random.shuffle(vertices)

    with click.progressbar(range(min(1000, len(vertices))), label='Calculating shortest paths for vetices') as bar:
        for i in bar:
            v = vertices[i]
            dist = shortest_distance(graph, source=v)

            for j in dist:
                frequency_dict[j] += 1

    n_paths = 0
    total = 0

    for i in range(100):
        n_paths += frequency_dict[i]
        total += frequency_dict[i] * i

    mean = total / n_paths

    return mean
