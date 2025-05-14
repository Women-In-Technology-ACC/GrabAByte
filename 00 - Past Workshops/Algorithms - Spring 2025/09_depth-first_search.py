# Depth-First Search

# A depth-first search is a graph traversal algorithm that explores
# as far along each branch as possible before backtracking, used
# for tasks like topological sortign and cycle detection

#################################################################

# FUNCTION TO PERFORM DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node] - visited:
        dfs(graph, neighbor, visited)
    return visited

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
result = dfs(graph, start_node)

# PRINT RESULTS
print("DFS Traversal Order:", result)