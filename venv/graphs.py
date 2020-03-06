from collections import namedtuple

# Vertex = namedtuple('Vertex', ['vertex', 'edge'])
# graph_3 = []
# graph_3.append([Vertex(1, 2), Vertex(2, 3)])
# graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
# graph_3.append([Vertex(0, 3), Vertex(1, 2)])
# graph_3.append([Vertex(1, 1)])
# print(*graph_3, sep='\n')

class Graph:
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge

g = Graph((1, 2), (2, 3))



