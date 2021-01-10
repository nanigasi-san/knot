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

def get_new_number(g: nx.MultiDiGraph) -> int:
    return max(g.nodes) + 1

def del_null_node(g: nx.MultiDiGraph) -> nx.MultiDiGraph:
    g = deepcopy(g)
    nns = [node[0] for node in g.nodes.data("parity") if node[1] is None]
    for nn in nns:
        succ = list(g.succ[nn])
        pred = list(g.pred[nn])
        if len(succ) == 1 and len(pred) == 1:
            g.remove_node(nn)
            g.add_edge(pred[0], succ[0])
        else:
            print("偶奇変わりそう")
    return g


def del_self_loop(g: nx.MultiDiGraph) -> nx.MultiDiGraph:
    g = deepcopy(g)
    edges = [edges[:2] for edges in g.edges]
    for e in edges:
        if e[0] == e[1]:
            sl_node = e[0]
            g.remove_edge(sl_node, sl_node)

            null_node_number = get_new_number(g)
            g.add_node(null_node_number, parity=None)
            g.add_edges_from([(null_node_number, sl_node), (sl_node, null_node_number)])

    return g
