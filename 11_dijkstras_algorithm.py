# Dijkstra's Algorithm

# A dijkstra's algorithm is a graph algorithm for finding the
# shortest path from a starting node to all other nodes in a 
# graph with non negative edge weights

#################################################################

import heapq

# FUNCTION TO PERFORM DIJKSTRA'S ALGORITHM
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# SET VARIABLES
# the graph and the starting node
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}
start_node = 'A'

# CALL THE FUNCTION
result = dijkstra(graph, start_node)

# PRINT RESULTS
print("Shortest distances from node", start_node, ":", result)