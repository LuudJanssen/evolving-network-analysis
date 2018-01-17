import networkx
import pandas

pagerank_key = 'pagerank'


# Calculates the pagerank for each node in a graph in a Pandas DataFrame
def graph_pagerank(graph):
    pagerank = networkx.pagerank_scipy(graph, alpha=0.85)

    pagerank_dataframe = pandas.DataFrame.from_dict(pagerank, orient='index')
    pagerank_dataframe.columns = [pagerank_key]

    return pagerank_dataframe


# Sorts all nodes on their pagerank
def sort_for_pagerank(dataframe):
    return dataframe.sort_values([pagerank_key], ascending=False)


