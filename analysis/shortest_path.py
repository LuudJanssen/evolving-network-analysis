import numpy
import graph_tool
from graph_tool.topology import shortest_distance


# Calculates the diameter of a graph
def graph_shortest_path(graph):
	return shortest_distance(graph)


# Returns the shortest paths for the given vertices
def shortest_paths_for_vertices(shortest_path, vertices):
    return shortest_path.get_2d_array(vertices)


# Gets the shortest paths mean
def shortest_paths_mean(graph, diameter):
	frequentyDict = {}
	
	# max path length equals the diameter 
	for i in range(diameter + 1):
		frequentyDict[i] = 0
	
	for v in graph.vertices():
		dist = shortest_distance(graph, source = v)
		for i in dist:
			frequentyDict[i] += 1
		print('1 source vertex done.')
	
	nPaths = 0
	total = 0
	for i in range(diameter + 1):
		nPaths += frequentyDict[i]
		total += frequentyDict[i] * i
	mean = total / nPaths
	
	return mean