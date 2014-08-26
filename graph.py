# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 20:43:07 2014

@author: Administrator
"""
import alg_module1_graphs

EX_GRAPH0 = {0: set([1,2]),
          1: set([]),
          2: set([])}

EX_GRAPH1 = {0: set([1,4,5]),
          1: set([2,6]),
          2: set([3]),
          3: set([0]),
          4: set([1]),
          5: set([2]),
          6: set([])}

EX_GRAPH2 = {0: set([1,4,5]),
          1: set([2,6]),
          2: set([3,7]),
          3: set([7]),
          4: set([1]),
          5: set([2]),
          6: set([]),
          7: set([3]),
          8: set([1,2]),
          9: set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes. 
    """
    graph = {}
    if num_nodes > 0:
        for dummy_i in range(num_nodes):
            edges = []
            for dummy_j in range(num_nodes):
                if dummy_i != dummy_j:
                    edges.append(dummy_j)
            graph[dummy_i] = set(edges)
    
    return graph

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph. 
    """
    in_degrees = {}
    keys = digraph.keys()
    for dummy_key in keys:
        edges = digraph[dummy_key]
        for dummy_edges in edges:
            if in_degrees.has_key(dummy_edges) == False:
                in_degrees[dummy_edges] = 1
            else:
                in_degrees[dummy_edges] += 1
    
    for dummy_key in keys:
        if in_degrees.has_key(dummy_key) == False:
            in_degrees[dummy_key] = 0
    return in_degrees

def in_degree_distribution(digraph):
    """
     Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the in-degrees of the graph. 
    """
    in_degrees = compute_in_degrees(digraph)
    distribution = {}
    for dummy_key in in_degrees.keys():
        if distribution.has_key(in_degrees[dummy_key]) == False:
            distribution[in_degrees[dummy_key]] = 1
        else:
            distribution[in_degrees[dummy_key]] += 1
#    for dummy_key in in_degree_distribution.keys():
#        in_degree_distribution[dummy_key] = (float)(in_degree_distribution[dummy_key]) / len(digraph)
    
    return distribution

#print compute_in_degrees(alg_module1_graphs.GRAPH1)