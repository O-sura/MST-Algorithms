from queue import PriorityQueue
import numpy as np
from graphGen import generate_graph

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.visited = False

    def connect(self, ad_vertex, edge_cost):
        global totalEdges
        self.edges.append(Edge(self, ad_vertex, edge_cost))
        ad_vertex.edges.append(Edge(ad_vertex, self, edge_cost))
        totalEdges += 2

    def __repr__(self):
        return self.name

class Edge:
    def __init__(self, _from, _to, _cost):
        self._from = _from
        self._to = _to
        self._cost = _cost

    def __lt__(self, other):
        if isinstance(other, Edge):
            return self._cost < other._cost
        return False

    def __repr__(self):
        return f"{self._from}-----{self._to}"

class Prims:
    def __init__(self):
        self.pqueue = PriorityQueue()
        self.mst = []
        self.totalCost = 0

    def findMST(self, s):
        global totalEdges

        self.addEdges(s)
        edgeCount = 0

        while not self.pqueue.empty() and edgeCount != totalEdges:
            minEdge = self.pqueue.get()

            if minEdge._to.visited:
                continue
            else:
                edgeCount += 1
                self.totalCost += minEdge._cost
                self.mst.append(minEdge)
                self.addEdges(minEdge._to)

        return edgeCount != totalEdges

    def addEdges(self, s):
        s.visited = True
        for edge in s.edges:
            if not edge._to.visited:
                self.pqueue.put(edge)

# Function to determine whether the input is an adjacency matrix or adjacency list
def is_adjacency_matrix(graph):
    return isinstance(graph, np.ndarray)

# Function to run Prim's algorithm on either adjacency matrix or adjacency list
def run_prims(graph):
    global totalEdges
    totalEdges = 0

    if is_adjacency_matrix(graph):
        num_nodes = len(graph)
        vertices = [Vertex(str(i)) for i in range(num_nodes)]

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if graph[i][j] > 0:
                    vertices[i].connect(vertices[j], graph[i][j])

    else:  # Assuming it's an adjacency list
        vertices = [Vertex(str(node)) for node in graph]

        for u, neighbors in graph.items():
            for v, edge_data in neighbors.items():
                vertices[int(u)].connect(vertices[int(v)], edge_data['weight'])

    prim = Prims()
    start_vertex = vertices[0]
    if prim.findMST(start_vertex):
        return prim.mst, prim.totalCost
    else:
        return "MST not possible, the graph may be disconnected"

#Driver Code
if __name__ == "__main__":

    num_nodes = 10
    is_dense = False
    use_matrix = True

    adjacency_data = generate_graph(num_nodes, is_dense, use_matrix)

    if use_matrix:
        print("Adjacency Matrix:")
        print(adjacency_data)
    else:
        print("Adjacency List (Node: {Neighbor: Weight}):")
        #print(adjacency_data)
        [print(i,':',j) for i, j in adjacency_data.items()]

    mst, total_cost = run_prims(adjacency_data)
    print("Minimum Spanning Tree Edges:")
    for edge in mst:
        print(edge)
    print("Total Cost:", total_cost)