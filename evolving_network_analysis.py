import click
import data
import graph
import output
from analysis.density import graph_density
from analysis.info import graph_info
from analysis.pagerank import graph_pagerank, sort_for_pagerank

results_folder = 'results'
pagerank_path = results_folder + '/pagerank.csv'

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


# Calculate graph density
def density():
    output.important('\nCalculating graph density...')
    output.dim('Graph density: ' + str(graph_density(graph)))


# Calculate graph pagerank
def pagerank():
    output.important('\nCalculating graph pagerank...')
    pagerank = graph_pagerank(graph)
    output.normal('Calculated pagerank.')
    output.normal('Sorting pagerank values...')
    pagerank = sort_for_pagerank(pagerank)
    output.normal('Writing pagerank results to file...')
    data.dataframe_to_csv(pagerank, pagerank_path, True)
    output.normal('Saved pagerank to "' + pagerank_path + '"')
    output.normal('10 nodes with the highest pagerank:')
    output.normal(pagerank.head(10))


analysis_options = {
    'everything': everything,
    'density': density,
    'pagerank':  pagerank
}

while True:
    analysis_type = click.prompt('\nWhat would you like to analyse? (everything, nothing, density, pagerank)',
                                 default='everything')

    if analysis_type == 'nothing':
        break
    else:
        analysis_function = analysis_options.get(analysis_type, None)

        if analysis_function is None:
            output.warning('\nYour selected analysis "' + analysis_type +
                           '" was not understood. If you want to exit, type "nothing".')
        else:
            analysis_function()
