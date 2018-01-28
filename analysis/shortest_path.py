import graph_tool
from graph_tool.topology import shortest_distance


# Calculates the diameter of a graph
def graph_shortest_path(graph):
    return shortest_distance(graph)
