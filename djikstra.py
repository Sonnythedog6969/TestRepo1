#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:42:40 2022

@author: matthewharrison
"""

from digraph_generator import VersatileDigraph

class ShortestPathDAG(VersatileDigraph):
    ''' DAG shortest path '''
    
    def __init__(self):
        '''Import init from DAG'''
        self.__edge_weights = {}
        self.__node_values = {}
        self.__edge_names = {}
        super().__init__()
    
    def shortcut(self, start, end):
        '''Find shortest path accounting for edge weight between 2 nodes'''
        dist = {node:float('inf') for node in self.get_nodes()}
        dist[start] = 0
        topsort = self.top_sort()
        for node in topsort:
            if node == end:
                break
            for v_node in self.successors(node):
                dist[v_node] = min(dist[v_node], dist[node] + self.get_edge_wt(node,v_node))
        return dist[end]