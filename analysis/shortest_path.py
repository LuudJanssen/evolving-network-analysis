import numpy
import graph_tool
from graph_tool.topology import shortest_distance


# Calculates the diameter of a graph
def graph_shortest_path(graph):
    return shortest_distance(graph)


# Returns the shortest paths for the given vertices
def shortest_paths_for_vertices(shortest_path, vertices):
    return shortest_path.get_2d_array(vertices)


# Gets the shortest paths mean
def shortest_paths_mean(shortest_paths):
    return shortest_paths.mean()
