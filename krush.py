class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskals(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((u, v, weight))
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    minimum_spanning_tree = []
    vertices = set(graph.keys())
    ds = DisjointSet(vertices)

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

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

minimum_spanning_tree = kruskals(graph)

print("Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(u, "--", v, ": weight =", weight)
