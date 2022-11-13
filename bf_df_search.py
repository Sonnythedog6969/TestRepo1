#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:36:06 2022

@author: matthewharrison
"""

from collections import deque
from topological_sort import SortableDigraph

class TraversableDigraph(SortableDigraph):
    '''DFS and BFS sorting'''
    def __init__(self):
        super().__init__()
        
    def dfs(self, start):
        '''Depth first search traversal of graph'''
        s_nodes = set()
        q_nodes = [start]
        while q_nodes:
            node = q_nodes.pop()
            if node in s_nodes:
                continue
            s_nodes.add(node)
            successors = self.successors(node)
            q_nodes.extend(successors)
            yield node
            
    def bfs(self, start):
        '''Breadth first search traversal of the graph'''
        s_nodes = set()
        q_nodes = deque([start])
        while q_nodes:
            node = q_nodes.popleft()
            for head in self.successors(node):
                if head in s_nodes:
                    continue
                s_nodes.add(head)
                q_nodes.append(head)
                yield node