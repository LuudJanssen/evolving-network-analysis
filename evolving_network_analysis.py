import click
import data
import output
from graph import random_graph, datafile_to_graph
from analysis.density import graph_density
from analysis.lcc import graph_lcc
from analysis.diameter import graph_diameter
from analysis.pagerank import graph_pagerank, sort_for_pagerank
from analysis.degree import graph_degree, sort_for_in_degree, sort_for_out_degree
from analysis.betweenness_centrality import graph_betweenness_centrality, sort_for_betweenness_centrality
from analysis.shortest_path import graph_shortest_path, shortest_paths_for_vertices, shortest_paths_mean

TEST = True

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

if TEST:
    # Create a random graph
    output.important('Creating a random connected graph with 100 nodes')
    graph = random_graph()
else:
    # Read the graph
    output.important('Reading graph data from "' + filename + '"...')
    graph = datafile_to_graph(filename)


# Output graph info
output.success('\nSuccessfully read graph. Info:')
output.dim(str(graph.num_edges()) + "  edges")
output.dim(str(graph.num_vertices()) + "  vertices")


# Calculate all graph properties
def everything():
    density()
    largest_connected_component()
    diameter()
    pagerank()
    degree()
    diameter()
    betweenness_centrality()
    mean_shortest_path()


# Calculate graph density
def density():
    output.important('\nCalculating graph density...')
    output.dim('Graph density: ' + str(graph_density(graph)))


# Calculate the largest connected component
def largest_connected_component():
    output.important('\nCalculating largest connected component...')
    lcc = graph_lcc(graph)
    output.dim('Largest connected component: ' + str(lcc.num_vertices()))


# Calculate (pseudo) diameter
def diameter():
    output.important('\nCalculating graph diameter...')
    output.dim('Graph diameter: ' + str(graph_diameter(graph)))


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


# Calculate betweenness centrality
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


# Calculate mean shortest path
def mean_shortest_path():
    output.important('\nCalculating shortest paths...')
    shortest_paths = graph_shortest_path(graph)
    output.important('Calculated shortest paths')
    output.important('Retreiving shortest paths as arrays')
    shortest_paths = shortest_paths_for_vertices(shortest_paths, graph.get_vertices())
    output.important('\nCalculating shortest path mean')
    output.important('Mean shortest path: ' + str(shortest_paths_mean(shortest_paths)))


analysis_options = {
    'everything': everything,
    'nothing': None,
    'density': density,
    'diameter': diameter,
    'largest-connected-component': largest_connected_component,
    'pagerank': pagerank,
    'degree': degree,
    'betweenness-centrality': betweenness_centrality,
    'mean-shortest-path': mean_shortest_path
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
