import numpy
import pandas
import graph_tool
from graph_tool.centrality import betweenness

betweenness_centrality_key = 'betweenness_centrality'


# Calculates the diameter of a graph
def graph_betweenness_centrality(graph):
    nodes, edges = betweenness(graph)

    nodes_dataframe = pandas.DataFrame(nodes.get_array())
    edges_dataframe = pandas.DataFrame(edges.get_array())

    nodes_dataframe.columns = [betweenness_centrality_key]
    edges_dataframe.columns = [betweenness_centrality_key]

    nodes_dataframe = sort_for_betweenness_centrality(nodes_dataframe)
    edges_dataframe = sort_for_betweenness_centrality(edges_dataframe)

    return nodes_dataframe, edges_dataframe


# Sort a dataframe containing node information for the in degree
def sort_for_betweenness_centrality(dataframe):
    return dataframe.sort_values([betweenness_centrality_key], ascending=False)
