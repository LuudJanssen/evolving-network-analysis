import graph_tool
import math


# Calculates the density of a graph
def graph_density(graph):
    if graph.num_edges() == 0:
        return None

    density = (graph.num_vertices() / (math.pow(graph.num_edges(), 2)))
    return density
