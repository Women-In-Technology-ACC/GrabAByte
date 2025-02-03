# Dynamic Programming (Knapsack Problem)

# A dynamic programming (knapsack problem) solves optimization
# problems by breaking them down into simpler subproblems and using
# stored solutions to avoid redundant calculations

#################################################################


# FUNCTION TO SOLVE KNAPSACK PROBLEM
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# SET VARIABLES
# the values, weights, and capacity
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# CALL THE FUNCTION
result = knapsack(values, weights, capacity)

# PRINT RESULTS
print("Maximum value in the knapsack:", result)