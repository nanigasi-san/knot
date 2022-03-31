from knot import KnotEulerianGraph, Port, Parity

def keg_to_graph(filepath: str):
    with open(filepath) as f:
        graph = KnotEulerianGraph()

        node_attrs_list = []
        edge_attrs_list = []

        lines = filter(None, map(lambda line : line.strip(), f.readlines()))

        process_node_flag = False
        process_edge_flag = False

        for line in lines:
            if line == "[nodes]":
                process_node_flag = True
                process_edge_flag = False
                continue
            elif line == "[edges]":
                process_node_flag = False
                process_edge_flag = True
                continue
            
            if process_node_flag:
                node_attrs_list.append(parse_node_attrs(line))
            elif process_edge_flag:
                edge_attrs_list.append(parse_edge_attrs(line))
        
        for node_attrs in node_attrs_list:
            graph.add_node(*node_attrs)

        for edge_attrs in edge_attrs_list:
            graph.add_edge(*edge_attrs)

    return graph

def parse_node_attrs(keg_node_repr):
    index, parity = keg_node_repr.split()
    index = int(index)
    if parity == "Odd":
        parity = Parity.Odd
    elif parity == "Even":
        parity = Parity.Even
    elif parity == "None":
        parity = Parity.Empty
    
    return [index, parity]

def parse_edge_attrs(keg_edge_repr):
    start_index, end_index, start_port, end_port = keg_edge_repr.split()
    start_index = int(start_index)
    end_index = int(end_index)

    if start_port == "A":
        start_port = Port.A
    elif start_port == "B":
        start_port = Port.B
    elif start_port == "None":
        start_port = Port.Empty

    if end_port == "A":
        end_port = Port.A
    elif end_port == "B":
        end_port = Port.B
    elif end_port == "None":
        end_port = Port.Empty

    return [start_index, end_index, start_port, end_port]

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

if __name__ == "__main__":
    print(keg_to_graph('../graphs/data/1.keg'))
