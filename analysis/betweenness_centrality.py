import graph_tool
from graph_tool.centrality import betweenness


# Calculates the diameter of a graph
def graph_betweenness_centrality(graph):
    return betweenness(graph)
