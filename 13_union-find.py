# Union-Find 

# A union-find algorithm is a data structure that efficiently 
# performs union and find operations, commonlhy used in algorithms
# like Kruskal's for minimum spanning tree.

#################################################################

# FUNCTION TO FIND PARENT
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# FUNCTION TO UNION TWO SETS
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

# SET VARIABLES
# the elements and their initial parent relationships
elements = [0, 1, 2, 3, 4]
parent = {x: x for x in elements}
rank = {x: 0 for x in elements}

# PERFORM UNION OPERATIONS
union(parent, rank, 0, 1)
union(parent, rank, 1, 2)

# FIND PARENTS
result = [find(parent, x) for x in elements]

# PRINT RESULTS
print("Parent of each element:", result)