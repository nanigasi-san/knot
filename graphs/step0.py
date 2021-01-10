import networkx as nx
from useful import *

g_0 = nx.MultiDiGraph()

add_node(g_0, 0, N)
add_node(g_0, 1, N)

add_edge(g_0, 0, 1, N, N)
add_edge(g_0, 1, 0, N, N)

if __name__ == "__main__":
    print_graph(g_0)
