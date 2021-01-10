import networkx as nx
from useful import *

g_1 = nx.MultiDiGraph()

add_node(g_1, 0,  N)
add_node(g_1, 1,  N)
add_node(g_1, 2,  Odd)

add_edge(g_1, 0, 2, N, A)
add_edge(g_1, 2, 1, B, N)
add_edge(g_1, 1, 2, N, B)
add_edge(g_1, 2, 0, A, N)

if __name__ == "__main__":
    print_graph(g_1)
