import networkx as nx
from copy import deepcopy
from time import sleep

def get_eulerian_circuit(g: nx.MultiDiGraph) -> tuple:
    ans = []
    g = deepcopy(g)
    first_edge = list(g.edges(data=True))[0]
    u, v, ABdata = first_edge
    for key, data in g[u][v].items():
        if data == ABdata:
            g.remove_edge(u, v, key=key)
            break
    ans.append(first_edge)
    now = v

    now_parity = g.nodes[now]["parity"]
    now_type = ABdata["Tv"]

    def get_next_type(now_parity, now_type):
        if now_parity == "Odd":
            if now_type == "A":
                return "B"
            elif now_type == "B":
                return "A"


        elif now_parity == "Even":
            if now_type == "A":
                return "A"
            elif now_type == "B":
                return "B"

        else:
            return None

    next_type = get_next_type(now_parity, now_type)
    while g.edges:
        flg = False
        for next, atlas_view in list(g.succ[now].items()):
            for key, data in list(atlas_view.items()):
                if data["Tu"] == next_type:
                    ans.append((now, next, data))
                    g.remove_edge(now, next, key=key)

                    now = next
                    now_parity = g.nodes[now]["parity"]
                    now_type = data["Tv"]
                    next_type = get_next_type(now_parity, now_type)
                    flg = True
                    break
            if flg:
                break
        else:
            print("miss!", ans)
            sleep(5)
            ok = False
            while not ok:
                edge = ans.pop(-1)
                u, v, edge_data = edge
                for next, atlas_view in list(g.succ[u].items()):
                    for key, data in list(atlas_view.items()):
                        if data["Tu"] == edge_data["Tu"]:
                            ans.append((u, next, data))
                            g.remove_edge(u, next, key=key)

                            now = next
                            now_parity = g.nodes[now]["parity"]
                            now_type = data["Tv"]
                            next_type = get_next_type(now_parity, now_type)

                            ok = True
                g.add_edge(u, v, **edge_data)

    return ans

def is_same_circuit(ec1, ec2) -> bool:
    for _ in range(len(ec2)):
        ec2.append(ec2.pop(0))
        if ec1 == ec2:
            return True
    else:
        return False

def is_same_graph(g1: nx.MultiDiGraph, g2: nx.MultiDiGraph) -> bool:
    ec1 = get_eulerian_circuit(g1)
    ec2 = get_eulerian_circuit(g2)
    return is_same_circuit(ec1, ec2)

def dell_null_node(g: nx.MultiDiGraph) -> nx.MultiDiGraph:
    g = deepcopy(g)
    edges = g.edges(data=True)
    # print(edges)
    for node, parity in g.nodes(data="parity"):
        if parity is None:
            pred, pred_data = list(dict(g.pred[node][0]).items())[0]
            succ, succ_data = list(dict(g.succ[node][0]).items())[0]
            g.remove_edge(pred, node)
            g.remove_edge(node, succ)
            g.add_edge(pred, succ, Tu=pred_data["Tu"], Tv=pred_data["Tv"])
    for node in g.nodes:
        if not (g.successors(node) and g.predecessors(node)):
            g.remove_node(node)
    return g
