import pandas

in_degree_key = 'in_degree'
out_degree_key = 'out_degree'


# Gets the degree information for each node in the graph
def graph_degree(graph):
    in_degrees = graph.in_degree()
    out_degrees = graph.out_degree()

    in_degrees_dataframe = pandas.DataFrame(
        [in_degree[1:] for in_degree in in_degrees],
        index=[in_degree[0] for in_degree in in_degrees])

    out_degrees_dataframe = pandas.DataFrame(
        [out_degree[1:] for out_degree in out_degrees],
        index=[out_degree[0] for out_degree in out_degrees])

    in_degrees_dataframe.columns = [in_degree_key]
    out_degrees_dataframe.columns = [out_degree_key]

    node_dataframe = in_degrees_dataframe.join(out_degrees_dataframe)

    return node_dataframe


# Sort a dataframe containing node information for the in degree
def sort_for_in_degree(dataframe):
    return dataframe.sort_values([in_degree_key], ascending=False)


# Sort a dataframe containing node information for the out degree
def sort_for_out_degree(dataframe):
    return dataframe.sort_values([out_degree_key], ascending=False)
