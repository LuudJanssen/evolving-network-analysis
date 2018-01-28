import click
import data
import graph
import output
from analysis.density import graph_density
from analysis.lcc import graph_lcc
from analysis.diameter import graph_diameter
from analysis.pagerank import graph_pagerank, sort_for_pagerank
from analysis.degree import graph_degree, sort_for_in_degree, sort_for_out_degree
from analysis.betweenness_centrality import graph_betweenness_centrality, sort_for_betweenness_centrality

results_folder = 'results'
pagerank_path = results_folder + '/pagerank.csv'
degree_path = results_folder + '/degree.csv'
nodes_betweenness_path = results_folder + '/betweenness.nodes.csv'
edges_betweenness_path = results_folder + '/betweenness.edges.csv'

# Add results folder
data.make_folder(results_folder)

# Import the data file
filename = 'tgraph_real_wikiedithyperlinks.txt'

# If no file was selected, exit
if filename == '':
    output.error('No data file selected, exiting...')
    exit()

# Read the graph
output.important('Reading graph data from "' + filename + '"...')
# graph = graph.datafile_to_graph(filename)
graph = graph.random_graph()

# Output graph info
output.success('\nSuccessfully read graph. Info:')
output.dim(str(graph.num_edges()) + "  edges")
output.dim(str(graph.num_vertices()) + "  vertices")

# calculate LCC
lcc = graph_lcc(graph)
output.dim('LCC:  ' + str(lcc.num_vertices()))


# Calculate all graph properties
def everything():
    density()
    pagerank()
    degree()
    diameter()


# Calculate graph density
def density():
    output.important('\nCalculating graph density...')
    output.dim('Graph density: ' + str(graph_density(graph)))


# Calculate (pseudo) diameter
def diameter():
    output.important('\nCalculating graph diameter...')
    output.dim('Graph diameter: ' + str(graph_diameter(lcc)))


# Calculate graph pagerank
def pagerank():
    output.important('\nCalculating graph pagerank...')
    pagerank_dataframe = graph_pagerank(graph)
    output.normal('Calculated pagerank.')
    output.normal('Sorting pagerank values...')
    pagerank_dataframe = sort_for_pagerank(pagerank_dataframe)
    output.normal('\n10 nodes with the highest pagerank:')
    output.normal(pagerank_dataframe.head(10))
    output.normal('\nWriting pagerank results to file...')
    data.dataframe_to_csv(pagerank_dataframe, pagerank_path, True)
    output.success('Saved pagerank results to "' + pagerank_path + '"')


# Calculate graph degree information
def degree():
    output.important('\nGathering graph degree information...')
    degree_dataframe = graph_degree(graph)
    output.normal('Gathered degree information.')
    output.normal('Sorting for in degree...')
    in_degree_sorted = sort_for_in_degree(degree_dataframe)
    output.normal('\n10 nodes with the highest in degree:')
    output.normal(in_degree_sorted.head(10))
    output.normal('\nSorting for out degree...')
    out_degree_sorted = sort_for_out_degree(degree_dataframe)
    output.normal('\n10 nodes with the highest out degree:')
    output.normal(out_degree_sorted.head(10))
    output.normal('\nWriting degree information to file...')
    data.dataframe_to_csv(in_degree_sorted, degree_path, True)
    output.success('Saved degree information to "' + degree_path + '"')


def betweenness_centrality():
    output.important('\nCalculating betweenness centrality...')
    nodes, edges = graph_betweenness_centrality(graph)
    output.normal('Calulated betweenness centrality for both edges and nodes.')
    output.normal('Sorting both datasets for betweenness centrality...')
    nodes = sort_for_betweenness_centrality(nodes)
    edges = sort_for_betweenness_centrality(edges)
    output.normal('\n10 nodes with the highest betweenness centrality:')
    output.normal(nodes.head(10))
    output.normal('\n10 edges with the highest betweenness centrality:')
    output.normal(edges.head(10))
    output.normal('\nWriting betweenness centrality ...')
    data.dataframe_to_csv(nodes, nodes_betweenness_path, True)
    output.success('Saved nodes betweenness centrality information to "' + nodes_betweenness_path + '"')
    data.dataframe_to_csv(edges, edges_betweenness_path, True)
    output.success('Saved edges betweenness centrality information to "' + edges_betweenness_path + '"')


analysis_options = {
    'everything': everything,
    'nothing': None,
    'density': density,
    'pagerank': pagerank,
    'degree': degree,
    'diameter': diameter,
    'betweenness-centrality': betweenness_centrality
}

while True:
    try:
        analysis_type = click.prompt('\nWhat would you like to analyse? (' + ', '.join(analysis_options.keys()) + ')',
                                     default='everything')
    except click.Abort:
        output.error('\n\nAborted, closing program...')
        exit()

    if analysis_type == 'nothing':
        break
    else:
        analysis_function = analysis_options.get(analysis_type, None)

        if analysis_function is None:
            output.warning('\nYour selected analysis "' + analysis_type +
                           '" was not understood. If you want to exit, type "nothing".')
        else:
            analysis_function()
