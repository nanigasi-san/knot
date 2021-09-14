class Edge:
    def __init__(self, edge_data: tuple[int, int, dict]):
        self.u = edge_data[0]
        self.v = edge_data[1]
        self.Tu = edge_data[2]["Tu"]
        self.Tv = edge_data[2]["Tv"]

    def __str__(self):
        return str((self.u, self.v, self.Tu, self.Tv))

    def __repr__(self):
        return self.__str__()
