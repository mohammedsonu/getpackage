def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[float('inf') if i != j else 0 for j in range(num_vertices)]
            for i in range(num_vertices)]

    for u in range(num_vertices):
        for v, weight in graph[u].items():
            dist[u][v] = weight

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example usage:
if __name__ == "__main__":
    # Sample graph representation (adjacency matrix)
    graph = {0: {1: 3, 2: 6, 3: 15}, 1: {2: -2}, 2: {3: 2}, 3: {}}

    shortest_paths = floyd_warshall(graph)
    for i in range(len(shortest_paths)):
        for j in range(len(shortest_paths[i])):
            print(
                f"Shortest path from vertex {i} to vertex {j}: {shortest_paths[i][j]}")
