import networkx as nx
from useful import *

# p1-2ab
g_3_3 = nx.MultiDiGraph()

add_node(g_3_3, 0, Even)
add_node(g_3_3, 1, Odd)
add_node(g_3_3, 2, Odd)


add_edge(g_3_3, 0, 1, B, A)
add_edge(g_3_3, 1, 2, B, A)
add_edge(g_3_3, 2, 0, B, A)
add_edge(g_3_3, 0, 2, A, A)
add_edge(g_3_3, 2, 1, B, B)
add_edge(g_3_3, 1, 0, A, B)
