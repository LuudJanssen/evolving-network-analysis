import graph_tool
from graph_tool.topology import pseudo_diameter


# Calculates the diameter of a graph
def graph_diameter(graph):
	return pseudo_diameter(graph)[0]
