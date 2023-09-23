from graphGen import generate_graph
from kruskals import Graph
from lazy_prims import run_prims
from eager_prims import Graph as Pgraph
import time
import random


# Example usage:
num_nodes = random.randint(5000,6000)
is_dense = True
use_matrix = True

adjacency_data = generate_graph(num_nodes, is_dense, use_matrix)
#Printing the generated graph
if use_matrix:
    print("Adjacency Matrix:")
    print(adjacency_data)
else:
    print("Adjacency List (Node: {Neighbor: Weight}):")
    #print(adjacency_data)
    [print(i,':',j) for i, j in adjacency_data.items()]
# print("Graph generated....")

# Record start time
start_time_kruskals = time.time()
#Kruskals algo results
graph = Graph(adjacency_data)
print("\nMinimum Spanning Tree (Kruskal's Algorithm):")
graph.kruskal_algo()

# Record end time
end_time_kruskals = time.time()

#duration
print("Start:\t",start_time_kruskals)
print("End:\t",end_time_kruskals)
duration_kruskals = end_time_kruskals - start_time_kruskals
print("Kruskal's Algorithm Duration:", duration_kruskals, "seconds")

print("\n\n\n")

# Record start time
start_time_lazy_prims = time.time()
#Prims Lazy version results
mst, total_cost = run_prims(adjacency_data)
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)
print("Total Cost:", total_cost)

# Record end time
end_time_lazy_prims = time.time()

#duration
print("Start:\t",start_time_lazy_prims)
print("End:\t",end_time_lazy_prims)
duration_lazy_prims = end_time_lazy_prims - start_time_lazy_prims
print("Prim's Lazy Version Duration:", duration_lazy_prims, "seconds")

print("\n\n\n")

# Record start time
start_time_eager_prims = time.time()
#Prims Eager version results
g = Pgraph(adjacency_data)
g.prim_mst()

# Record end time
end_time_eager_prims = time.time()

#duration
print("Start:\t",start_time_eager_prims)
print("End:\t",end_time_eager_prims)
duration_eager_prims = end_time_eager_prims - start_time_eager_prims
print("Prim's Eager Version Duration:", duration_eager_prims, "seconds")