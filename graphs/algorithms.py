import networkx as nx
from copy import deepcopy
from step0 import g_0
from step1 import g_1
from step2 import g_2_1, g_2_2, g_2_3
from step3 import g_3_3
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

    print("Nodes:", g.nodes(data=True))
    print("EulerC:", ans)
    print("-"*50)
get_eulerian_circuit(g_0)
get_eulerian_circuit(g_1)
get_eulerian_circuit(g_2_1)
get_eulerian_circuit(g_2_2)
get_eulerian_circuit(g_2_3)
get_eulerian_circuit(g_3_3)