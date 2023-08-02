
import sys


def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Maintain a set of visited nodes
    visited = set()

    while True:
        # Find the node with the minimum distance from the start node
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            # No more nodes to visit
            break

        visited.add(min_node)

        # Update distances to neighboring nodes
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


# Example graph representation using adjacency list
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

# Print the shortest distances from the start node to all other nodes
for node, distance in distances.items():
    print(f'Shortest distance from {start_node} to {node}: {distance}')
