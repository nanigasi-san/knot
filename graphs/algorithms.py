import networkx as nx
from copy import deepcopy
from time import sleep
from useful import convert_edges, print_graph


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

    def get_next_type(now_parity: str, now_type: str):
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
            sleep(1)
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
    # edges = g.edges(data=True)
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


def r1_minus(g: nx.MultiDiGraph) -> nx.MultiDiGraph:
    g = g.copy()
    del_nodes = []
    for node, parity in g.nodes(data="parity"):
        # print(node, parity)
        if (parity == "Odd") and (node in g.neighbors(node)):
            data = g[node][node][0]
            if data["Tu"] != data["Tv"]:
                for pred_node, data in g.pred[node].items():
                    if pred_node != node:
                        u = pred_node
                        Tu = data[0]["Tu"]
                for succ_node, data in g.succ[node].items():
                    if succ_node != node:
                        v = succ_node
                        Tv = data[0]["Tv"]
                # print(u, v, Tu, Tv)
                del_nodes.append(node)
                g.add_edge(u, v, Tu=Tu, Tv=Tv)
    for node in del_nodes:
        g.remove_node(node)
    return g


"""
1: 空のグラフオブジェクトXを用意する
2: 元のグラフGの適当な辺をひとつ選ぶ。その辺の始点を頂点番号0としてXに追加する(頂点の偶奇はそのまま写す)
3: 2.で選んだ辺からGのオイラー閉路を辿る。
4: 途中で新しい頂点(Xに追加されていない頂点)を通ったら連番で番号をつける。この時、先に入ったA(またはB)をAとする。この時、最初の辺は頂点0のBから出ているとする。
5: 4.のルールを守りながら通った辺をXに辺を追加していく
"""


def rebuild(g: nx.MultiDiGraph):
    ans = []
    rev = {"A": "B", "B": "A"}
    ec = get_eulerian_circuit(g)
    for _ in range(len(ec)):
        node_dict = {}
        ec.append(ec.pop(0))
        x = nx.MultiDiGraph()
        u, v, data = ec[0]
        Tu = data["Tu"]
        Tv = data["Tv"]
        node_dict[u] = (0, (Tu == "B"))
        x.add_node(0, parity=g.nodes[u]["parity"])
        if v not in node_dict:
            node_dict[v] = (1, Tv == "A")
            x.add_node(1, parity=g.nodes[v]["parity"])
        nu, ab_same_u = node_dict[u]
        nv, ab_same_v = node_dict[v]
        nTu = Tu if ab_same_u else rev[Tu]
        nTv = Tv if ab_same_v else rev[Tv]
        x.add_edge(nu, nv, Tu=nTu, Tv=nTv)

        for ec_edge in ec[1:]:
            u, v, data = ec_edge
            Tu = data["Tu"]
            Tv = data["Tv"]
            if v not in node_dict:
                node_dict[v] = (x.number_of_nodes(), (Tv == "A"))
                x.add_node(x.number_of_nodes(), parity=g.nodes[v]["parity"])
            nu, ab_same_u = node_dict[u]
            nv, ab_same_v = node_dict[v]
            nTu = Tu if ab_same_u else rev[Tu]
            nTv = Tv if ab_same_v else rev[Tv]
            x.add_edge(nu, nv, Tu=nTu, Tv=nTv)
        ans.append(x)
    return ans


def integration_nodes(g):
    def is_connect(p1, p2):
        c1 = len(g[p1][p2]) if p2 in g.succ[p1] else 0
        c2 = len(g[p2][p1]) if p1 in g.succ[p2] else 0
        if c1 == 2:
            return True, 1
        elif c2 == 0:
            return True, 1
        elif c1 == 1 and c2 == 1:
            return True, 2
        else:
            return False, 0

    for p1, data1 in g.nodes(data="parity"):
        for p2, data2 in g.nodes(data="parity"):
            conn, conn_type = is_connect(p1, p2)
            if conn:
                if conn_type == 1:  # a
                    pass
                else:  # b
                    pass
    """
    a, b, c, dの割り振り、後はやるだけ
    """
    return g


def s_plus(input_g: nx.MultiDiGraph) -> list[nx.MultiDiGraph]:
    """
    拡張済みのグラフに対してS+をする関数。
    """
    output = []
    ec = convert_edges(get_eulerian_circuit(input_g))
    n = len(ec)
    extend_ec = ec * 2
    for i in range(n-1):
        for j in range(1, n):
            print(f"step{i}-{j} start.")
            print_graph(input_g)
            start_edge = extend_ec[i]
            end_edge = extend_ec[i+j]
            a, b, Ta, Tb = tuple(start_edge)
            c, d, Tc, Td = tuple(end_edge)
            g = deepcopy(input_g)

            nn = g.number_of_nodes()  # number_of_nodes
            g.add_node(nn, parity="Odd")

            g.add_edge(a, nn, Tu=Ta, Tv="A")
            g.add_edge(b, nn, Tu=Tb, Tv="B")
            g.add_edge(nn, c, Tu="B", Tv=Tc)
            g.add_edge(nn, d, Tu="A", Tv=Td)

            g.remove_edge(a, b)
            g.remove_edge(c, d)

            for k in range(i+1, i+j-1):
                edge = ec[k]
                u, v, Tu, Tv = tuple(edge)
                g.add_edge(v, u, Tu=Tv, Tv=Tu)
                g.remove_edge(u, v)
                """
                TODO: これ同じ辺が二個あって片方が範囲から出ていたらバグりませんか。消す前に辺の数を調べ、二個以上あるときは消さないほう(消す辺と一致しないもの)を保持し、remove_edgeの後で同じ辺を追加する。
                """
            output.append(g)
            print(f"step{i}-{j} is done.")
            print_graph(g)
    return output
