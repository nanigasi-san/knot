from algorithms import rebuild
from convert import keg_to_graph
from useful import convert_edges_for_list_of_tuple

g1 = keg_to_graph("data/rebuild/2_1.keg")
x1 = rebuild(g1)
print("=====")
g2 = keg_to_graph("data/rebuild/2_2.keg")
x2 = rebuild(g2)

i = x1[0]
for j in x2:
    nodes_eq = (sorted(i.nodes(data=True)) == sorted(j.nodes(data=True)))
    edges_eq = (sorted(convert_edges_for_list_of_tuple(i.edges(data=True))) == sorted(convert_edges_for_list_of_tuple(j.edges(data=True))))
    if nodes_eq and edges_eq:
        print("Yes")
    else:
        print("No")
