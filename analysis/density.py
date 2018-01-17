import networkx


# Calculates the density of a graph
def graph_density(graph):
    return networkx.density(graph)
