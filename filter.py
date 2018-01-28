import numpy
from graph import time_start_key, time_end_key


def start_time(graph, start_time):
    start_filter = graph.new_edge_property('bool')
    start_filter.a = graph.edge_properties[time_start_key].a <= start_time

    graph.set_edge_filter(start_filter)

    return start_filter


def end_time(graph, end_time):
    end_filter = graph.new_edge_property('bool')
    end_filter.a = graph.edge_properties[time_end_key].a > end_time

    graph.set_edge_filter(end_filter)

    return end_filter


def at_time(graph, time):
    start_filter = start_time(graph, time)
    end_filter = end_time(graph, time)

    time_filter = graph.new_edge_property('bool')
    time_filter.a = numpy.logical_and(start_filter.a, end_filter.a)

    graph.set_edge_filter(time_filter)


def unset(graph):
    graph.set_edge_filter(None)


def time_max(graph):
    return graph.edge_properties[time_end_key].a.max()


def time_min(graph):
    return graph.edge_properties[time_start_key].a.min()
