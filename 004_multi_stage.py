import sys

def multistage_graph(graph):
    num_stages = len(graph)

    # Cost table to store the optimal cost to reach each node
    cost = [0] * num_stages

    # Parent table to store the optimal path
    parent = [0] * num_stages

    # Initialize the cost table for the last stage
    for i in range(num_stages - 2, -1, -1):
        min_cost = sys.maxsize
        best_node = -1

        for j in range(num_stages):
            if graph[i][j] + cost[j] < min_cost:
                min_cost = graph[i][j] + cost[j]
                best_node = j

        cost[i] = min_cost
        parent[i] = best_node

    return cost, parent

def print_optimal_path(parent):
    path = [0]
    current_node = parent[0]

    while current_node != 0:
        path.append(current_node)
        current_node = parent[current_node]

    path.append(0)
    path.reverse()

    return path

# Example usage:
graph = [
    [0, 1, 2, 5, 0, 0],
    [0, 0, 0, 0, 4, 1],
    [0, 0, 0, 0, 2, 3],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

cost, parent = multistage_graph(graph)

print("Optimal Cost to reach each node:", cost)
print("Optimal Path:", print_optimal_path(parent))
