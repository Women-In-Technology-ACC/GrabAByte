# Kruskal's Algorithm

# A Kruskal's algorithm is a greedy algorithm for finding the
# minimum spannign tree of a graph by selecting the edges with the
# smallest weights and avoiding cycles

#################################################################

# FUNCTION TO PERFORM KRUSKAL'S ALGORITHM
def kruskal(graph):
    edges = sorted(graph['edges'], key=lambda x: x[2])
    parent = {x: x for x in graph['vertices']}
    rank = {x: 0 for x in graph['vertices']}
    mst = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst

# SET VARIABLES
# the graph with vertices and edges
graph = {
    'vertices': ['A', 'B', 'C', 'D'],
    'edges': [
        ('A', 'B', 1),
        ('A', 'C', 5),
        ('B', 'C', 3),
        ('B', 'D', 4),
        ('C', 'D', 2)
    ]
}

# CALL THE FUNCTION
result = kruskal(graph)

# PRINT RESULTS
print("Minimum Spanning Tree:", result)