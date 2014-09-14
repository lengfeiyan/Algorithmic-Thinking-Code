# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 21:00:06 2014

@author: Administrator
"""
import graph
import random
import matplotlib.pyplot as plt

def upa(n,m):
    result_graph = graph.make_complete_graph(m)
    for i in range(m,n):
        edeg = []
        for count in range(m):
            edeg.append(random.choice(result_graph.keys()))
        result_graph[i] = set(edeg)
        
    return result_graph
    
if __name__ == "__main__":
    g = upa(27770,13)
    edeg_num = 0
    for key in g.keys():
        edeg_num += len(g[key])
    
    distribution = graph.in_degree_distribution(g)
    for dummy_key in distribution.keys():
        distribution[dummy_key] = (float)(distribution[dummy_key]) / 27770
    plt.loglog(distribution.keys(),distribution.values())
    