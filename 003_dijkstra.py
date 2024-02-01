import heapq

def dijkstra(graph, start_node):
    # Initialize data structures
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Use a priority queue to keep track of nodes and their distances
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Check if the current distance is already updated
        if current_distance > distances[current_node]:
            continue

        # Update distances for neighboring nodes
        for neighbor, edge_weight in graph[current_node]:
            distance = current_distance + edge_weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph_dijkstra = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)],
}

start_node_dijkstra = 'A'
shortest_distances = dijkstra(graph_dijkstra, start_node_dijkstra)

print("Shortest Distances from", start_node_dijkstra + ":")
for node, distance in shortest_distances.items():
    print(f"To {node}: {distance}")
