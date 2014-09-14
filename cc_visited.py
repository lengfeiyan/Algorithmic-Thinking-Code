# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 12:09:47 2014

@author: Administrator
"""

from collections import deque
import alg_module2_graphs

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node 
    and returns the set consisting of all nodes that are visited by a breadth-first search that starts at start_node.
    """
    queue = deque()
    visited = [start_node]
    queue.append(start_node)
    while len(queue) > 0:
        pop_node = queue.pop()
        neighbors = ugraph[pop_node]
        for node in neighbors:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    
    return set(visited)

def cc_visited(ugraph) :
    """
    Takes the undirected graph ugraph and returns a list of sets, 
    where each set consists of all the nodes (and nothing else) in a connected component, 
    and there is exactly one set in the list for each connected component in ugraph and nothing else.
    """
    remaing_nodes = ugraph.keys()
    connected_component = []
    while len(remaing_nodes) > 0:
        current_node = remaing_nodes[0]
        visited = bfs_visited(ugraph,current_node)
        connected_component.append(visited)
        remaing_nodes_new = []
        for node in remaing_nodes:
            if node not in visited:
                remaing_nodes_new.append(node)
        remaing_nodes = remaing_nodes_new
    return connected_component

def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of the largest connected component in ugraph.
    """
    connected_component = cc_visited(ugraph)
    result = 0
    for dummy_cc in connected_component:
        if len(dummy_cc) > result:
            result = len(dummy_cc)
    
    return result

def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and iterates through the nodes in attack_order. 
    For each node in the list, the function removes the given node and its edges from the graph and 
    then computes the size of the largest connected component for the resulting graph.
    """
    print ugraph
    result = []
    result.append(largest_cc_size(ugraph))
    for dummy_node in attack_order:
        new_graph = {}
        for dummy_key in ugraph.keys():
            if dummy_key != dummy_node:
                values = ugraph[dummy_key]
                try:
                    values.remove(dummy_node)
                except KeyError:
                    pass
                new_graph[dummy_key] = values
        ugraph = new_graph
        result.append(largest_cc_size(ugraph))
        
    return result

print compute_resilience(alg_module2_graphs.GRAPH0, [1, 2]) 