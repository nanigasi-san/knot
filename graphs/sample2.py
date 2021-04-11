from algorithms import integration_nodes
from convert import keg_to_graph
from useful import convert_edges_for_list_of_tuple, print_graph

import networkx as nx
g = keg_to_graph("data/integration/1_1.keg")
x = integration_nodes(g)
# print_graph(x)
