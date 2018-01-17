import networkx


# Reads an edge list and interprets it as a multi directional graph with time attributes
def datafile_to_graph(filename):
    return networkx.read_edgelist(path=filename,
                                  create_using=networkx.MultiDiGraph(),
                                  data=(('start', int), ('end', int)))
