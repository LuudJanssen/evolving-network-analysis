import click
import data
import graph
import output
from analysis.info import graph_info
from analysis.density import graph_density
from analysis.pagerank import graph_pagerank, sort_for_pagerank
from analysis.degree import graph_degree, sort_for_in_degree, sort_for_out_degree

results_folder = 'results'
pagerank_path = results_folder + '/pagerank.csv'
degree_path = results_folder + '/degree.csv'

# Add results folder
data.make_folder(results_folder)

# Let the user select a data file
filename = data.select_data_file()

# If no file was selected, exit
if filename == '':
    output.error('No data file selected, exiting...')
    exit()

# Read the graph
output.important('Reading graph data from "' + filename + '"...')
graph = graph.datafile_to_graph(filename)

# Output graph info
output.success('\nSuccessfully read graph. Info:')
output.dim(graph_info(graph))


# Calculate all graph properties
def everything():
    density()
    pagerank()
    degree()


# Calculate graph density
def density():
    output.important('\nCalculating graph density...')
    output.dim('Graph density: ' + str(graph_density(graph)))


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
    data.dataframe_to_csv(in_degree_sorted, pagerank_path, True)
    output.success('Saved degree information to "' + pagerank_path + '"')


analysis_options = {
    'everything': everything,
    'nothing': None,
    'density': density,
    'pagerank':  pagerank,
    'degree': degree
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
