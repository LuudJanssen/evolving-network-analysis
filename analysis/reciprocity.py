from graph_tool.topology import edge_reciprocity


# Returns a graph's edge reciprocity
def graph_reciprocity(graph):
    return edge_reciprocity(graph)