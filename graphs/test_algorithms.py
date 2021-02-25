import convert
from algorithms import get_eulerian_circuit, is_same_circuit
from glob import glob

filenames = glob("data/*.keg")

def test_graph_to_circuit():
    for fn in filenames:
        g, ec = convert.keg_to_graph_and_ec(fn)
        assert is_same_circuit(ec, get_eulerian_circuit(g))
