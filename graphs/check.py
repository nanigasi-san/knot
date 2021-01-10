import convert
from algorithms import get_eulerian_circuit, is_same_circuit

filenames = ["0", "1", "2_1", "2_2", "2_3"]

for fn in filenames:
    g, ec = convert.kng_to_graph_and_ec(f"./data/{fn}.kng")
    print(fn, is_same_circuit(ec, get_eulerian_circuit(g)))
