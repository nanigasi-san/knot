import networkx as nx
from useful import *

# OO
g_2_1 = nx.MultiDiGraph()

add_node(g_2_1, 0, N)
add_node(g_2_1, 1, Odd)
add_node(g_2_1, 2, Odd)
add_node(g_2_1, 3, N)

add_edge(g_2_1, 0, 1, N, A)
add_edge(g_2_1, 1, 2, B, A)
add_edge(g_2_1, 2, 3, B, N)
add_edge(g_2_1, 3, 2, N, B)
add_edge(g_2_1, 2, 1, A, B)
add_edge(g_2_1, 1, 0, A, N)


# OE
g_2_2 = nx.MultiDiGraph()

add_node(g_2_2, 0, Odd)
add_node(g_2_2, 1, Even)

add_edge(g_2_2, 0, 1, B, B)
add_edge(g_2_2, 1, 0, B, A)
add_edge(g_2_2, 0, 1, B, A)
add_edge(g_2_2, 1, 0, A, A)


# OOE
g_2_3 = nx.MultiDiGraph()

add_node(g_2_3, 0, Odd)
add_node(g_2_3, 1, Odd)
add_node(g_2_3, 2, Even)

add_edge(g_2_3, 0, 1, B, A)
add_edge(g_2_3, 1, 2, B, A)
add_edge(g_2_3, 2, 1, A, B)
add_edge(g_2_3, 1, 0, A, B)
add_edge(g_2_3, 0, 2, A, B)
add_edge(g_2_3, 2, 0, B, A)


if __name__ == "__main__":
    print_graph(g_2_1)
    print_graph(g_2_2)
    print_graph(g_2_3)