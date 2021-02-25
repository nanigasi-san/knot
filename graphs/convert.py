import networkx as nx

def keg_to_graph(filepath: str) -> nx.MultiDiGraph:
    g = nx.MultiDiGraph()
    nodes_now, edges_now = False, False
    with open(filepath) as f:
        data = f.readlines()
        for l in data:
            l = l.strip()
            if not l:
                continue
            elif l == "[nodes]":
                nodes_now = True
            elif l == "[edges]":
                nodes_now = False
                edges_now = True

            elif nodes_now:
                u, parity = l.split()
                u = int(u)
                parity = parity if parity in {"Odd", "Even"} else None
                g.add_node(u, parity=parity)


            elif edges_now:
                u, v, Tu, Tv = l.split()
                u = int(u)
                v = int(v)
                Tu = Tu if Tu in {"A", "B"} else None
                Tv = Tv if Tv in {"A", "B"} else None
                g.add_edge(u, v, Tu=Tu, Tv=Tv)
    return g

def ec_to_eulerian_circuit(filepath: str) -> list:
    ec = []
    with open(filepath) as f:
        data = f.readlines()
        for l in data:
            l = l.strip()
            if not l:
                continue
            else:
                u, v, Tu, Tv = l.split()
                u = int(u)
                v = int(v)
                Tu = Tu if Tu in {"A", "B"} else None
                Tv = Tv if Tv in {"A", "B"} else None
                ec.append((u, v, {"Tu": Tu, "Tv": Tv}))
    return ec
