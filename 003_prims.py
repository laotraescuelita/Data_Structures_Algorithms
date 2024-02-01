import heapq
from collections import defaultdict

def prim(graph):
    # Initialize data structures
    visited = set()
    min_spanning_tree = []

    # Start with an arbitrary node (0 in this case)
    start_node = list(graph.keys())[0]

    # Use a priority queue to keep track of edges and their weights
    priority_queue = [(0, start_node, None)]

    while priority_queue:
        weight, current_node, prev_node = heapq.heappop(priority_queue)
        #print( weight, current_node, prev_node )

        if current_node not in visited:
            visited.add(current_node)
            if prev_node is not None:
                min_spanning_tree.append((prev_node, current_node, weight))

            for neighbor, edge_weight in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

    return min_spanning_tree

# Example usage:
graph_prim ={
    'A': [('B', 2), ('D', 3)],
    'B': [('A', 2), ('C', 5), ('D', 1)],
    'C': [('B', 5), ('D', 4)],
    'D': [('A', 3), ('B', 1), ('C', 4)],
}

min_spanning_tree_prim = prim(graph_prim)
print("Minimum Spanning Tree (Prim's Algorithm):", min_spanning_tree_prim)
