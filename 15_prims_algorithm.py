# Prim's Algorithm

# A prim's algorithm is a greedy algorithm for finding the minimum
# spanning tree by building the tree vertex at a time, starting 
# from an initial node

#################################################################



import heapq

# FUNCTION TO PERFORM PRIM'S ALGORITHM
def prim(graph, start):
    mst = []
    visited = set()
    edges = [(0, start, None)]

    while edges:
        weight, node, parent = heapq.heappop(edges)
        if node not in visited:
            visited.add(node)
            if parent is not None:
                mst.append((parent, node, weight))
            for neighbor, cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, neighbor, node))

    return mst

# SET VARIABLES
# the graph and the starting node
graph = {
    'A': {'B': 1, 'C': 5},
    'B': {'A': 1, 'C': 3, 'D': 4},
    'C': {'A': 5, 'B': 3, 'D': 2},
    'D': {'B': 4, 'C': 2}
}
start_node = 'A'

# CALL THE FUNCTION
result = prim(graph, start_node)

# PRINT RESULTS
print("Minimum Spanning Tree:", result)