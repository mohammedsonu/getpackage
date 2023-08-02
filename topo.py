
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]


# Example usage:
graph = {
    'A': ['D'],
    'B': ['D'],
    'C': ['A', 'B'],
    'D': ['E'],
    'E': []
}

sorted_nodes = topological_sort(graph)

print("Topological order:")
for node in sorted_nodes:
    print(node)
