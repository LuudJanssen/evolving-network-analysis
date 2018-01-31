from graph_tool.correlations import assortativity


# Calculate graph assortativity using the total degree
def graph_assortativity(graph):
    return assortativity(graph, 'total')
