#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:29:59 2022

@author: matthewharrison
"""

from digraph_generator import VersatileDigraph

class SortableDigraph(VersatileDigraph):
    '''topological sorting tree inherited from VersatileDigraph'''
    
    def __init__(self):
        super().__init__()
        
    def top_sort(self):
        '''returns topologically sorted list of nodes'''
        nodes = list(super().get_nodes())
        if len(nodes) == 0:
            raise IndexError('The graph does not have any defined nodes.')
        in_degrees = []
        for node in nodes:
            in_degrees.append(super().in_degree(node))
        count = {}
        for i in range(len(nodes)):
            count[nodes[i]] = in_degrees[i]
        q_nodes = [u for u in nodes if count[u] == 0]
        s_nodes = []
        while q_nodes:
            sort_node = q_nodes.pop()
            s_nodes.append(sort_node)
            successors = super().successors(sort_node)
            for node in successors:
                count[node] -= 1
                if count[node] == 0:
                    q_nodes.append(node)
        return s_nodes