import networkx
import pandas

betweenness_centrality_key = ['betweenness_centrality']


# Calculates the betweenness centrality for each node in a graph
def graph_betweenness_centrality(graph):
    betweenness_centrality = networkx.betweenness_centrality(graph)

    betweenness_centrality_dataframe = pandas.DataFrame.from_dict(betweenness_centrality, orient='index')
    betweenness_centrality_dataframe.columns = [betweenness_centrality_key]

    return betweenness_centrality_dataframe


# Sort for betweenness centrality in a Pandas DataFrame
def sort_for_betweenness_centrality(dataframe):
    return dataframe.sort_values([betweenness_centrality_key], ascending=False)
