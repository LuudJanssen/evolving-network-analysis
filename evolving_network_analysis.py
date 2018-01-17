import data
import graph
import output
from analysis.density import graph_density
from analysis.info import graph_info
from analysis.pagerank import graph_pagerank, sort_for_pagerank

results_folder = 'results'
pagerank_path = results_folder + '/pagerank.csv'

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

# Calculate graph density
output.important('\nCalculating graph density...')
output.dim('Graph density: ' + str(graph_density(graph)))

# Calculate graph pagerank
output.important('\nCalculating graph pagerank...')
pagerank = graph_pagerank(graph)
output.normal('Calculated pagerank. Sorting pagerank values...')
pagerank = sort_for_pagerank(pagerank)
output.normal('Writing pagerank results to file...')
data.dataframe_to_csv(pagerank, pagerank_path)
output.normal('Saved pagerank to "' + pagerank_path + '"')