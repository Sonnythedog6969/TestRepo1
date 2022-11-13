#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:48:12 2022

@author: matthewharrison
"""

from graphviz import Digraph
from bokeh.plotting import figure, show
from bokeh.palettes import Spectral6

class VersatileDigraph:
    '''Creates a versatile digraph'''
    
    def __init__(self):
        self.__edge_weights = {}
        self.__node_values = {}
        self.__edge_names = {}
        self.__edge_head = {}
        
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
            
    def add_node(self, node_id, node_value=0):
        '''Add node'''
        if isinstance(node_id, str) is not True:
            raise TypeError("Nodes must be entered as a string.")
        if isinstance(node_value, int) is not True:
            raise TypeError("Node values must be entered as an integer.")
        if node_value < 0:
            raise ValueError("Node values must be greater than or equal to 0.")
        self.__node_values[node_id] = node_value
        self.__edge_weights[node_id] = {}
        self.__edge_names[node_id] = {}
        self.__edge_head[node_id] = {}
        
    def get_nodes(self):
        '''Get node values'''
        return self.__edge_names.keys()
    
    def get_edge_wt(self, start, end):
        '''Get an edge weight'''
        return self.__edge_weights[start][end]
    
    def get_node_value(self, node):
        '''Get node information'''
        if not node in self.get_nodes():
            raise KeyError('Node ' + node + ' is not present in the graph.')
        return self.__node_values[node]
    
    def print_graph(self):
        '''Print all graph information'''
        for tail in self.get_nodes():
            print("Node " + str(tail) + " has a value of " + str(self.get_node_value(tail)) + ".")
            for head in self.__edge_weights[tail]:
                print("There is an edge from node " + str(tail) + " to node " + str(head) \
                      + " of weight " + str(self.get_edge_wt(tail,head)) + " and name " \
                          + self.__edge_names[tail][head] + ".")
                    
    def predecessors(self, node):
        '''Given a node, return a list of nodes that immediately preceed that node'''
        return [n for n in self.get_nodes() if node in self.__edge_names[n]]
    
    def successors(self, node):
        '''Given a node, return a list of nodes that immediately succeed that node'''
        return list(self.__edge_names[node].keys())
    
    def successor_on_edge(self, start_node, edge_name):
        '''Given node and edge name, identify successor on named edge'''
        if start_node not in self.__edge_names.keys():
            raise KeyError("That node does not exist in the digraph.")
        for head, tail_dict in self.__edge_names.items():
            for end_node, name in tail_dict.items():
                if head == start_node:
                    if name == edge_name:
                        print(end_node)
                        
    def in_degree(self, node):
        '''Return number of edges that lead to a node'''
        return len(self.predecessors(node))
    
    def out_degree(self, node):
        '''return number of edges that lead from a node'''
        if node not in self.__edge_weights.keys():
            raise KeyError("That node does not exist in the digraph.")
        out_nodes = []
        for head, tail_dict in self.__edge_weights.items():
            for tail, weight in tail_dict.items():
                if head == node:
                    out_nodes.append(tail)
        return len(out_nodes)
    
    def plot(self):
        '''Plot the digraph'''
        gr = Digraph()
        for head, tail_dict in self.__edge_weights.items():
            for tail, weight in tail_dict.items():
                gr.edge(head,tail,label=str(weight))
        gr.view()
        
    def edge_weight_plot(self):
        '''Bar graph of edge weights'''
        x_values = []
        y_values = []
        for head, tail_dict in self.__edge_weights.items():
            for tail, weight in tail_dict.items():
                y_values.append(weight)
                x_values.append(head + " to " + tail)
        p = figure(x_range = x_values, height = 400, width = 800, \
                   title = "Digraph Edge Weight Plot")
        p.vbar(x=x_values, top=y_values, width = 0.5, line_color = 'white', \
               color = Spectral6, hover_line_color = 'darkgrey')
        p.xaxis.major_label_orientation = "vertical"
        show(p)

