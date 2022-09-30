import networkx as nx
from data_structure import Edge

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


def convert_edges(edges: list[tuple[int, int, dict]]) -> list[Edge]:
    ans = []
    for edge in list(edges):
        ans.append(Edge(edge))
    return ans
