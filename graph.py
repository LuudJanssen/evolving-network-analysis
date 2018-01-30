import graph_tool
import graph_tool.generation as generation

time_start_key = 'time_start'
time_end_key = 'time_end'


# Reads an edge list and interprets it as a multi directional graph with time attributes
def datafile_to_graph(filename):
    return graph_tool.load_graph_from_csv(filename,
                                          directed=True,
                                          string_vals=False,
                                          eprop_types=['int', 'int'],
                                          eprop_names=[time_start_key, time_end_key],
                                          csv_options={
                                              "delimiter": " "
                                          })


def random_graph():
    return generation.complete_graph(1000)
