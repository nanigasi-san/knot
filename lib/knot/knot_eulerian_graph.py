from .edge import Edge
from .node import Node, Parity, Port

class KnotEulerianGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.is_valid = False
    
    def add_node(self, index, parity):
        node = Node(index, parity)
        self.nodes[index] = node

    def get_node(self, index):
        return self.nodes[index]

    def add_edge(self, start_index, end_index, start_port, end_port):
        start_node = self.get_node(start_index)
        end_node = self.get_node(end_index)

        edge = Edge(start_node, end_node, start_port, end_port)
        self.edges.append(edge)
    
    def validate(self):
        # ToDo
        self.is_valid = True
