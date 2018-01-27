import graph_tool
import math

# Calculates the density of a graph
def graph_density(graph):
    density = ( graph.num_vertices() / ( math.pow(graph.num_edges(),2) ) )
    return density
