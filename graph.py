import graph_tool
import graph_tool.generation as generation


# Reads an edge list and interprets it as a multi directional graph with time attributes
def datafile_to_graph(filename):
    return graph_tool.load_graph_from_csv(filename, directed=True, csv_options={
        "delimiter": " "
    })


def random_graph():
    return generation.complete_graph(100)
