from algorithms import s_plus
from convert import keg_to_graph
from useful import print_graph

g = keg_to_graph("./data/0.keg")
# print_graph(g)
s_g = s_plus(g)
# for i in s_g:
#     print_graph(i)
