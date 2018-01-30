from graph_tool.inference import minimize_blockmodel_dl, modularity, BlockState
import filter


# Calculates graph modularity using minimized nested blockmodel dl
def graph_modularity(graph):
    #filter.at_time(graph, 1033613761)
    state = minimize_blockmodel_dl(graph)
    #filter.unset(graph)
    print(state.get_bclabel())
    print(state.get_bpclabel())
    return state, modularity(state.get_bg(), state.get_bpclabel())
