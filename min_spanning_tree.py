#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:45:08 2022

@author: matthewharrison
"""

from heapq import heappop, heappush
from graphviz import Graph
from bf_df_search import TraversableDigraph

class SpanningTreeGraph(TraversableDigraph):
    '''Gives minimal spanning tree from Prim's algorithm and plots min tree graph'''
    
    def __init__(self):
        self.__edge_weights = {}
        self.__node_values = {}
        self.__edge_names = {}
        self.__edge_head = {}
        super().__init__()
        
    def add_edge(self,tail, head, **vararg):
        '''Adds an edge to the graph'''
        if isinstance(tail, str) is not True:
            raise TypeError("Nodes must be entered as a string.")
        if isinstance(head, str) is not True:
            raise TypeError("Nodes must be entered as a string.")
        if not tail in self.get_nodes():
            self.add_node(tail,vararg.get("start_node_value",0))
        if not head in self.get_nodes():
            self.add_node(head,vararg.get("end_node_value",0))
        edge_name = vararg.get("name",tail + " to " + head)
        self.__edge_names[tail][head] = edge_name
        if isinstance(edge_name, str) is not True:
            raise TypeError("Edge names must be entered as a string.")
        self.__edge_head[tail][edge_name] = head
        if isinstance(head, str) is not True:
            raise TypeError("Edge names must be entered as a string.")
        if vararg.get('weight', 0) >= 0:
            self.__edge_weights[tail][head] = vararg.get('weight',0)
        if vararg.get('weight', 0) >= 0:
            self.__edge_weights[head][tail] = vararg.get('weight',0)
        
    def spanning_tree(self, start):
        '''Minimal spanning tree'''
        parents = {}
        queue = [(0, None, start)]
        graph = Graph()
        while queue:
            _, p_node, u_node = heappop(queue)
            if u_node in parents:
                continue
            parents[u_node] = p_node
            for v_node in self.successors(u_node):
                weight = self.get_edge_wt(u_node, v_node)
                heappush(queue, (weight, u_node, v_node))
        new_p = {end:start for end, start in parents.items() if start is not None}
        for child, parent in new_p.items():
            graph.edge(parent, child, label = str(self.get_edge_wt(parent,child)))
        graph.view()