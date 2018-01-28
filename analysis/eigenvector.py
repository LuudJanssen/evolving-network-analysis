import graph_tool
import pandas

eigenvector_key = 'eigenvector'


# Calculates the eigenvector for each node in a graph in a Pandas DataFrame
def graph_eigenvector(graph):
    eigenvalue, eigenvectors = graph_tool.centrality.eigenvector(graph)

    eigenvector_dataframe = pandas.DataFrame(eigenvectors.get_array())
    eigenvector_dataframe.columns = [eigenvector_key]

    eigenvector_dataframe = sort_for_eigenvector(eigenvector_dataframe)

    return eigenvalue, eigenvector_dataframe


# Sorts all nodes on their eigenvector
def sort_for_eigenvector(dataframe):
    return dataframe.sort_values([eigenvector_key], ascending=False)
