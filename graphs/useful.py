import networkx as nx
from copy import deepcopy

A = "A"
B = "B"
N = None
Odd = "Odd"
Even = "Even"

def add_node(g: nx.MultiDiGraph, node: int, parity) -> None:
    g.add_node(node, parity=parity)

def add_edge(g: nx.MultiDiGraph, u: int, v: int, Tu, Tv) -> None:
    g.add_edge(u, v, Tu=Tu, Tv=Tv)

def print_graph(g: nx.MultiDiGraph) -> None:
    print("Nodes:", [(node, g.nodes[node]["parity"]) for node in g.nodes])
    print("Edges:", [(edge[0], edge[1], *list(g.get_edge_data(*edge[:2])[0].values())) for edge in g.edges])

def convert_edges_for_list_of_tuple(edges):
    ans = []
    for edge in list(edges):
        u, v, data = edge
        Tu = data["Tu"]
        Tv = data["Tv"]
        new_edge = (u, v, Tu, Tv)
        ans.append(new_edge)
    return ans