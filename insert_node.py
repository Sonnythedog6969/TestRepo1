#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:26:36 2022

@author: matthewharrison
"""

from digraph_generator import VersatileDigraph

class BinaryTree(VersatileDigraph):
    '''Binary Digraph implementing methods from superclass VersatileDigraph'''
    
    def __init__(self, rootvalue=0):
       super().__init__()
       self.add_node('Root', rootvalue)
       
    def add_node_left(self, child, child_value, parent='Root'):
        '''Add a node to the left of parent node'''
        super().add_node(child, child_value)
        super().add_edge(parent, child, name='left')
        
    def add_node_right(self, child, child_value, parent='Root'):
        '''Add a node to the left of parent node'''
        super().add_node(child, child_value)
        super().add_edge(parent, child, name='right')
        
    def get_node_left(self, node):
        '''Get left child node'''
        super().successor_on_edge(node, 'left')
        
    def get_node_right(self, node):
        '''Get right child node'''
        super().successor_on_edge(node, 'right')