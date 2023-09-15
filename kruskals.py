
from graphGen import generate_graph

class Graph:
    def __init__(self, representation):
        if isinstance(representation, list):
            # If representation is a list, assume it's an adjacency list
            self.graph = self.convert_adjacency_list_to_matrix(representation)
        else:
            # Otherwise, assume it's an adjacency matrix
            self.graph = representation

        self.V = len(self.graph)

    # Helper function to convert adjacency list to adjacency matrix
    def convert_adjacency_list_to_matrix(self, adjacency_list):
        V = len(adjacency_list)
        adjacency_matrix = [[0] * V for _ in range(V)]
        for u, neighbors in enumerate(adjacency_list):
            for v, weight in neighbors.items():
                adjacency_matrix[u][v] = weight
        return adjacency_matrix

    # Search function
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Applying Kruskal algorithm
    def kruskal_algo(self):

        result = []
        i, e = 0, 0
        edges = []
        
        if isinstance(self.graph, dict):
            # Process adjacency list
            for u in range(self.V):
                for v, weight_info in self.graph[u].items():
                    v_weight = weight_info['weight']
                    edges.append((u, v, v_weight))

            edges = sorted(edges, key=lambda item: item[2])

            parent = list(range(self.V))
            rank = [0] * self.V

            while e < self.V - 1:
                u, v, w = edges[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent, v)
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    self.apply_union(parent, rank, x, y)

            for u, v, weight in result:
                print("%d - %d: %d" % (u, v, weight))
            
        else:
            # Process adjacency matrix
            for u in range(self.V):
              for v in range(u + 1, self.V):
                  v_weight = self.graph[u][v]
                  if v_weight != 0:
                      edges.append((u, v, v_weight))
            
            edges = sorted(edges, key=lambda item: item[2])

            parent = list(range(self.V))
            rank = [0] * self.V

            while e < self.V - 1:
                u, v, w = edges[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent, v)
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    self.apply_union(parent, rank, x, y)

            for u, v, weight in result:
                print("%d - %d: %d" % (u, v, weight))



# Example usage:
num_nodes = 10
is_dense = False
use_matrix = False

adjacency_data = generate_graph(num_nodes, is_dense, use_matrix)

if use_matrix:
    print("Adjacency Matrix:")
    print(adjacency_data)
else:
    print("Adjacency List (Node: {Neighbor: Weight}):")
    #print(adjacency_data)
    [print(i,':',j) for i, j in adjacency_data.items()]

graph = Graph(adjacency_data)
print("\nMinimum Spanning Tree (Kruskal's Algorithm):")
graph.kruskal_algo()