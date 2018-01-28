import graph_tool
import pandas

pagerank_key = 'pagerank'


# Calculates the pagerank for each node in a graph in a Pandas DataFrame
def graph_pagerank(graph):
    pagerank = graph_tool.centrality.pagerank(graph)

    pagerank_dataframe = pandas.DataFrame(pagerank.get_array())
    pagerank_dataframe.columns = [pagerank_key]

    pagerank_dataframe = sort_for_pagerank(pagerank_dataframe)

    return pagerank_dataframe


# Sorts all nodes on their pagerank
def sort_for_pagerank(dataframe):
    return dataframe.sort_values([pagerank_key], ascending=False)
