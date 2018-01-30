import graph_tool
from graph_tool.topology import pseudo_diameter
from analysis.lcc import graph_lcc


# Calculates the diameter of a graph
def graph_diameter(graph):
	largest_connected_component = graph_lcc(graph)
	return int(pseudo_diameter(largest_connected_component)[0])
