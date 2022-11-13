#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:16:03 2022

@author: matthewharrison
"""

from insert_node import BinaryTree

class SortingTree(BinaryTree):
    '''sorting a binary tree'''
    
    def __init__(self,root_value=0):
       super().__init__()
       
    def insert(self,value,node='Root'):
        '''add node. child < parent = left, child > parent = right'''
        if value > self.get_node_value(node):
            if self.get_node_left(node) is None:
                self.add_node_left("n"+str(value), value, node)
            else:
                self.insert(value, self.get_node_left(node))
        elif value <= self.get_node_value(node):
            if self.get_node_right(node) is None:
                self.add_node_right("n"+str(value), value, node)
            else:
                self.insert(value, self.get_node_right(node))
                
    def traverse(self,node):
        '''in-order tree traversal for sorted node values'''
        if self.get_node_left(node='Root') is not None:
            self.traverse(self.get_node_left(node))
        print(self.get_node_value(node), end=' ')
        if self.get_node_right(node) is not None:
            self.traverse(self.get_node_right(node))