import graph_tool
from graph_tool.topology import label_largest_component


# Calculates the lcc of a graph
def graph_lcc(graph):
	map = label_largest_component(graph, True)
	lcc = graph_tool.GraphView(graph, vfilt=map)
	return lcc