import heapq
import numpy as np
from graphGen import generate_graph

class Graph:
    def __init__(self, representation):
        self.V = len(representation)
        self.graph = [[] for _ in range(self.V)]

        if isinstance(representation, np.ndarray):
          # Check if it's an adjacency matrix
          if len(representation.shape) == 2 and representation.shape[0] == representation.shape[1]:
              for i in range(self.V):
                for j in range(i + 1, self.V):
                    weight = representation[i][j]
                    if weight > 0:
                        self.add_edge(i, j, weight)
    
        else:
          for node, neighbors in representation.items():
            for neighbor, weight_dict in neighbors.items():
                weight = weight_dict['weight']
                self.add_edge(node, neighbor, weight)

        

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        in_mst = [False] * self.V
        min_heap = []

        key[0] = 0
        heapq.heappush(min_heap, (0, 0))

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            in_mst[u] = True

            for v, w in self.graph[u]:
                if not in_mst[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
                    heapq.heappush(min_heap, (key[v], v))

        # Print the MST edges and their weights
        total_weight = 0
        for i in range(1, self.V):
            total_weight += key[i]
            print(f"Edge: {parent[i]} - {i}, Weight: {key[i]}")

        print(f"Total Weight of MST: {total_weight}")


# Create a graph from the adjacency data and run MST algorithm
num_nodes = 10
is_dense = True
use_matrix = False

adjacency_data = generate_graph(num_nodes, is_dense, use_matrix)

if use_matrix:
    print("Adjacency Matrix:")
    print(adjacency_data)
else:
    print("Adjacency List (Node: {Neighbor: Weight}):")
    #print(adjacency_data)
    [print(i,':',j) for i, j in adjacency_data.items()]

g = Graph(adjacency_data)
g.prim_mst()