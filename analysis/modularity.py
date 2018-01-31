# Returns igraph partitions
def graph_partitions(graph):
    return graph.community_multilevel()


# Calculates modularity using igraph given a graph and partitions
def graph_modularity(graph, partitions):
    return graph.modularity(partitions)
