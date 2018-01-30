import click
import data
import output
import filter
from graph import random_graph, datafile_to_graph
from analysis.density import graph_density
from analysis.lcc import graph_lcc
from analysis.diameter import graph_diameter
from analysis.pagerank import graph_pagerank
from analysis.degree import graph_degree, sort_for_in_degree, sort_for_out_degree, sort_for_degree_sum
from analysis.betweenness_centrality import graph_betweenness_centrality
from analysis.shortest_path import shortest_paths_mean
from analysis.eigenvector import graph_eigenvector

TEST = False
STATIC_ANALYSIS = True
TEMPORAL_ANALYSIS = True
NSnapshots = 10

results_folder = 'results'
pagerank_path = results_folder + '/pagerank'
degree_path = results_folder + '/degree'
nodes_betweenness_path = results_folder + '/betweenness.nodes'
edges_betweenness_path = results_folder + '/betweenness.edges'
eigenvector_path = results_folder + '/eigenvector'

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


# Returns the filename for a CSV file with a given timestamp
def get_timestamp_path(path, timestamp=None):
    postfix = '.csv'

    if timestamp is None:
        return path + '.static' + postfix
    else:
        return path + '.' + str(timestamp) + postfix


# Generates a timestamp string depending on the existence timestamp
def get_timestamp_sting(timestamp=None):
    timestamp_string = ''

    if timestamp is not None:
        timestamp_string = ' at ' + str(timestamp)

    return timestamp_string


# Calculate all graph properties
def everything(timestamp=None):
    density(timestamp)
    largest_connected_component(timestamp)
    diameter(timestamp)
    pagerank(timestamp)
    degree(timestamp)
    diameter(timestamp)
    betweenness_centrality(timestamp)
    mean_shortest_path(timestamp)
    eigenvector(timestamp)


# Calculate graph density
def density(timestamp=None):
    output.important('\nCalculating graph density...')
    output.dim('Graph density' + get_timestamp_sting(timestamp) + ': ' + str(graph_density(graph)))


# Calculate the largest connected component
def largest_connected_component(timestamp=None):
    output.important('\nCalculating largest connected component...')
    lcc = graph_lcc(graph)
    output.dim('Largest connected component' + get_timestamp_sting(timestamp) + ': ' + str(lcc.num_vertices()) +
               ' vertices and ' + str(lcc.num_edges()) + ' edges.')


# Calculate (pseudo) diameter
def diameter(timestamp=None):
    output.important('\nCalculating graph diameter...')
    output.dim('Graph diameter' + get_timestamp_sting(timestamp) + ': ' + str(graph_diameter(graph)))


# Calculate graph pagerank
def pagerank(timestamp=None):
    output.important('\nCalculating graph pageranks' + get_timestamp_sting(timestamp) + '...')
    pagerank_dataframe = graph_pagerank(graph)
    output.normal('Calculated pageranks.')
    output.normal('\n10 nodes with the highest pagerank' + get_timestamp_sting(timestamp) + ':')
    output.normal(pagerank_dataframe.head(10))
    output.normal('\nWriting pagerank results to file...')
    data.dataframe_to_csv(pagerank_dataframe, get_timestamp_path(pagerank_path, timestamp), True)
    output.success('Saved pagerank results to "' + get_timestamp_path(pagerank_path, timestamp) + '"')


# Calculate graph degree information
def degree(timestamp=None):
    output.important('\nGathering graph degree information' + get_timestamp_sting(timestamp) + '...')
    degree_dataframe = graph_degree(graph)
    output.normal('Gathered degree information.')
    output.normal('Sorting for in degree...')
    in_degree_sorted = sort_for_in_degree(degree_dataframe)
    output.normal('\n10 nodes with the highest in degree' + get_timestamp_sting(timestamp) + ':')
    output.normal(in_degree_sorted.head(10))
    output.normal('\nSorting for out degree...')
    out_degree_sorted = sort_for_out_degree(degree_dataframe)
    output.normal('\n10 nodes with the highest out degree' + get_timestamp_sting(timestamp) + ':')
    output.normal(out_degree_sorted.head(10))
    output.normal('\nSorting for degree sum...')
    sum_degree_sorted = sort_for_degree_sum(degree_dataframe)
    output.normal('\n10 nodes with the highest degree sum' + get_timestamp_sting(timestamp) + ':')
    output.normal(sum_degree_sorted.head(10))
    output.normal('\nWriting degree information to file...')
    data.dataframe_to_csv(sum_degree_sorted, get_timestamp_path(degree_path, timestamp), True)
    output.success('Saved degree information to "' + get_timestamp_path(degree_path, timestamp) + '"')


# Calculate betweenness centrality
def betweenness_centrality(timestamp=None):
    output.important('\nCalculating betweenness centralities' + get_timestamp_sting(timestamp) + '...')
    nodes, edges = graph_betweenness_centrality(graph)
    output.normal('Calulated betweenness centralities for both edges and nodes.')
    output.normal('\n10 nodes with the highest betweenness centrality' + get_timestamp_sting(timestamp) + ':')
    output.normal(nodes.head(10))
    output.normal('\n10 edges with the highest betweenness centrality' + get_timestamp_sting(timestamp) + ':')
    output.normal(edges.head(10))
    output.normal('\nWriting betweenness centralities to file..')
    data.dataframe_to_csv(nodes, get_timestamp_path(nodes_betweenness_path, timestamp), True)
    output.success('Saved nodes betweenness centrality information to "' +
                   get_timestamp_path(nodes_betweenness_path, timestamp) + '"')
    data.dataframe_to_csv(edges, get_timestamp_path(edges_betweenness_path, timestamp), True)
    output.success('Saved edges betweenness centrality information to "' +
                   get_timestamp_path(edges_betweenness_path, timestamp) + '"')


# Calculate mean shortest path
def mean_shortest_path(timestamp=None):
    output.important('\nCalculating shortest paths' + get_timestamp_sting(timestamp) + '...')
    lcc = graph_lcc(graph)
    mean = shortest_paths_mean(lcc)
    output.normal('Calculated shortest paths')
    output.normal('mean shortest path length' + get_timestamp_sting(timestamp) + ': ' + mean)


# Calculate graph pagerank
def eigenvector(timestamp=None):
    output.important('\nCalculating graph eigenvectors' + get_timestamp_sting(timestamp) + '...')
    eigenvalue, eigenvector_dataframe = graph_eigenvector(graph)
    output.normal('Calculated eigenvectors.')
    output.dim('Largest eigenvalue' + get_timestamp_sting(timestamp) + ': ' + str(eigenvalue))
    output.normal('\n10 nodes with the highest eigenvector' + get_timestamp_sting(timestamp) + ':')
    output.normal(eigenvector_dataframe.head(10))
    output.normal('\nWriting eigenvector results to file...')
    data.dataframe_to_csv(eigenvector_dataframe, get_timestamp_path(eigenvector_path, timestamp), True)
    output.success('Saved eigenvector results to "' + get_timestamp_path(eigenvector_path, timestamp) + '"')


analysis_options = {
    'everything': everything,
    'nothing': None,
    'density': density,
    'diameter': diameter,
    'largest-connected-component': largest_connected_component,
    'pagerank': pagerank,
    'degree': degree,
    'betweenness-centrality': betweenness_centrality,
    'mean-shortest-path': mean_shortest_path,
    'eigenvector': eigenvector
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
            if STATIC_ANALYSIS:
                output.important('\n-- STATIC ANALYIS --')
                analysis_function()

            if TEMPORAL_ANALYSIS:
                output.important('\n-- TEMPORAL ANALYIS --')

                time_start = filter.time_min(graph)
                time_end = filter.time_max(graph)
                time_diff = time_end - time_start

                output.normal('First edge time: ' + str(time_start))
                output.normal('Last edge time: ' + str(time_end))
                output.normal('Time difference: ' + str(time_diff))

                snapshots = click.prompt('\nHow many snapshots should be analysed?', default=10, type=int)

                for number in range(snapshots):
                    current_time = time_start + int(round(time_diff / (snapshots - 1) * number))

                    output.important('\n- Temporal analysis ' + str(number + 1) + '/' + str(snapshots) +
                                     ' | timestamp: ' + str(current_time))

                    filter.at_time(graph, current_time)

                    analysis_function(current_time)

                    filter.unset(graph)
