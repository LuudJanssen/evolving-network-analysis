import pandas

in_degree_key = 'in_degree'
out_degree_key = 'out_degree'
sum_degree_key = 'degree_sum'


# Gets the degree information for each node in the graph
def graph_degree(graph):
    in_degrees = graph.get_in_degrees(graph.get_vertices())
    out_degrees = graph.get_out_degrees(graph.get_vertices())

    in_degrees_dataframe = pandas.DataFrame(in_degrees)
    out_degrees_dataframe = pandas.DataFrame(out_degrees)

    in_degrees_dataframe.columns = [in_degree_key]
    out_degrees_dataframe.columns = [out_degree_key]

    node_dataframe = in_degrees_dataframe.join(out_degrees_dataframe)
    node_dataframe[sum_degree_key] = node_dataframe[in_degree_key] + node_dataframe[out_degree_key]

    return node_dataframe


# Sort a dataframe containing node information for the in degree
def sort_for_in_degree(dataframe):
    return dataframe.sort_values([in_degree_key], ascending=False)


# Sort a dataframe containing node information for the out degree
def sort_for_out_degree(dataframe):
    return dataframe.sort_values([out_degree_key], ascending=False)


# Sort a dataframe containing node information for the degree sum
def sort_for_degree_sum(dataframe):
    return dataframe.sort_values([sum_degree_key], ascending=False)
