
import heapq


def prims(graph):
    start_node = next(iter(graph))
    visited = set([start_node])
    min_heap = [(weight, start_node, neighbor)
                for neighbor, weight in graph[start_node]]
    heapq.heapify(min_heap)
    minimum_spanning_tree = []

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        if v not in visited:
            visited.add(v)
            minimum_spanning_tree.append((u, v, weight))

            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, v, neighbor))

    return minimum_spanning_tree


# Example usage:
graph = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('H', 11), ('C', 8)],
    'C': [('B', 8), ('I', 2), ('D', 7), ('F', 4)],
    'D': [('C', 7), ('F', 14), ('E', 9)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('I', 6), ('H', 1)],
    'H': [('A', 8), ('B', 11), ('I', 7), ('G', 1)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}

minimum_spanning_tree = prims(graph)

print("Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(u, "--", v, ": weight =", weight)
