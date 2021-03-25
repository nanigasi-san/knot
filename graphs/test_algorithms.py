from convert import keg_to_graph, ec_to_eulerian_circuit
from algorithms import get_eulerian_circuit, is_same_circuit, is_same_graph, dell_null_node
from glob import glob


def test_graph_to_circuit():
    keg_paths = glob("data/*.keg")
    ec_paths = glob("data/*.ec")
    for keg_path, ec_path in zip(keg_paths, ec_paths):
        g = keg_to_graph(keg_path)
        ec = ec_to_eulerian_circuit(ec_path)
        assert is_same_circuit(get_eulerian_circuit(g), ec)

def test_is_same_graph():
    g1 = keg_to_graph("data/is_same_graph/1_1.keg")
    g2 = keg_to_graph("data/is_same_graph/1_2.keg")
    assert is_same_graph(g1, g2)

def test_del_null_nodes():
    g1 = keg_to_graph("data/eq/null/1_1.keg")
    g2 = keg_to_graph("data/eq/null/1_2.keg")
    assert is_same_graph(dell_null_node(g1), g2)