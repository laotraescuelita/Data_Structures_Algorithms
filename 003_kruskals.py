def kruskal(graph):
    # Initialize data structures
    parent = {}
    rank = {}
    min_spanning_tree = []

    # Helper functions for Union-Find operations
    def find_set(node):
        if parent[node] != node:
            parent[node] = find_set(parent[node])
        return parent[node]

    def union_sets(node1, node2):
        root1 = find_set(node1)
        root2 = find_set(node2)

        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                rank[root2] += 1

    # Initialize disjoint sets for each node
    for node in graph:
        parent[node] = node
        rank[node] = 0

    # Sort edges by weight
    edges = [(weight, node1, node2) for node1, neighbors in graph.items() for node2, weight in neighbors]
    edges.sort()

    # Process edges in ascending order
    for weight, node1, node2 in edges:
        if find_set(node1) != find_set(node2):
            min_spanning_tree.append((node1, node2, weight))
            union_sets(node1, node2)

    return min_spanning_tree

# Example usage:
graph_kruskal = {
    'A': [('B', 2), ('D', 3)],
    'B': [('A', 2), ('C', 5), ('D', 1)],
    'C': [('B', 5), ('D', 4)],
    'D': [('A', 3), ('B', 1), ('C', 4)],
}

min_spanning_tree_kruskal = kruskal(graph_kruskal)
print("Minimum Spanning Tree (Kruskal's Algorithm):", min_spanning_tree_kruskal)
