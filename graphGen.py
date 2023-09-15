import networkx as nx
import numpy as np
import random

def generate_graph(num_nodes, is_dense=True, use_matrix=True):
    if is_dense:
        # Create a dense graph
        G = nx.dense_gnm_random_graph(num_nodes, num_nodes*(num_nodes-1)//2)
    else:
        # Create a sparse graph
        G = nx.gnm_random_graph(num_nodes, num_nodes*2)

    # Assign random weights to edges
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(-20, 20)

    if use_matrix:
        # Convert to adjacency matrix
        adjacency_matrix = np.zeros((num_nodes, num_nodes))
        for u, v in G.edges():
            adjacency_matrix[u][v] = G[u][v]['weight']
            adjacency_matrix[v][u] = G[u][v]['weight']
        return adjacency_matrix
    else:
        # Convert to adjacency list
        adjacency_list = {node: {} for node in range(num_nodes)}
        for u, v in G.edges():
            adjacency_list[u][v] = {'weight': G[u][v]['weight']}
            adjacency_list[v][u] = {'weight': G[u][v]['weight']}
        return adjacency_list



