import convert
from algorithms import get_eulerian_circuit, is_same_circuit
from glob import glob

keg_paths = glob("data/*.keg")
ec_paths = glob("data/*.ec")

def test_graph_to_circuit():
    for keg_path, ec_path in zip(keg_paths, ec_paths):
        g = convert.keg_to_graph(keg_path)
        ec = convert.ec_to_eulerian_circuit(ec_path)
        assert is_same_circuit(get_eulerian_circuit(g), ec)
