# Breadth-First Search

# A breadth-first search is a graph traversal algorithm that 
# explores all neighbors of a node level by level often used
# for finding the shortest path in unweighted graphs

#################################################################


from collections import deque

# FUNCTION TO PERFORM BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(graph[node] - visited)

    return traversal_order

# SET VARIABLES
# the graph and the starting node
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
start_node = 'A'

# CALL THE FUNCTION
result = bfs(graph, start_node)

# PRINT RESULTS
print("BFS Traversal Order:", result)