## Projects Object Oriented Programming with Python
  * The included files are based on topics covered in my programming algorithms course. Essentially you are able to create a directed or undirected graph and perform actions upon that graph, such as applying sorting algorithms, visualization, or finding maximum flow for example. Based on the below order, the files use inheritance to utilize previously defined methods starting first with digraph_generator.py, which contains the VersatileDigraph class. The VersatileDigraph class has all methods necessary to create a class, and return initial information. The following classes define other algorithms and methods to further enhance this initial class. 

### digraph_generator.py
  * Creates a directed graph by storing given nodes in dicts. Also receives variable information such as edge weight, node name, edge name, etc.
  * Use add_node and add_edge methods to create the graph
  * Further methods to return requested information from the graph, such as  number of in nodes, successors, etc.
  * plot method uses graphviz to visualize graph and edge_weight_plot method uses Bokeh to return a bar plot of edge weights 
  * All other files in this repository use classes that inherit and build off of this initial digraph_generator
  
### insert_node.py
  * adds a node left if it is less than the parent node
  * adds a node right if it is greater than parent node
  * ultimately creates a binary sorted tree
  
### in_order_sorting_tree.py
  * uses in-order sorting to sort the binary tree from insert_node.py by decreasing node value 
  
### topological_sort.py
  * uses topological sorting to display nodes by dependency
  
### bf_df_search.py
  * dfs - uses depth first search to sort a directed graph
  * bfs - uses breadth first search to sort a directed graph
  
### djikstra.py
  * Djikstra's algorithm using topological sorting inherited from topological_sort.py to return shortest path in a directed graph from start node to end node
  
### min_spanning_tree.py
  * Uses Prim's algorithm to find the minimum spanning tree in an undirected graph
  
