# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 21:00:06 2014

@author: Administrator
"""
import graph
import random
import matplotlib.pyplot as plt

def dpa(n,m):
    result_graph = graph.make_complete_graph(m)
#    in_degrees = graph.compute_in_degrees(result_graph)
#        totindeg = 0
#        for node in in_degrees.keys():
#            totindeg += in_degrees[node]
    for i in range(m,n):
        edeg = []
#        for node in result_graph.keys():
#            alpha = random.random()
#            p = (float)(in_degrees[node] + 1 ) / (totindeg + i)
#            if alpha < p:
#                edeg.append(node)
        for count in range(m):
            edeg.append(random.choice(result_graph.keys()))
        result_graph[i] = set(edeg)
        
    return result_graph
    
if __name__ == "__main__":
    g = dpa(27770,13)
    edeg_num = 0
    for key in g.keys():
        edeg_num += len(g[key])
    
    distribution = graph.in_degree_distribution(g)
    for dummy_key in distribution.keys():
        distribution[dummy_key] = (float)(distribution[dummy_key]) / 27770
    plt.loglog(distribution.keys(),distribution.values())
    