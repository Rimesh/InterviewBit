# Given a two-dimensional square matrix cost[][] of order M*N
# where cost[i][j] represents the cost of passing through cell(i, j).
# Total cost to reach a particular cell is the sum of costs of all the
# cells in that path (including the starting and the final cell).
# we can only move either downward or rightward.

# Write a function that returns the minimum cost of moving from the
# top-left cell to bottom-right cell of the matrix.

cost = [[1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]]

# Recursive approach
# ------------------------------------------------------

def minimumPath(cost, m, n):

    # base condition
    if m == 0 and n == 0:
        return cost[0][0]

    # boundry conditions
    # 1. This is the first row of cost matrix.
    if m == 0:
        return cost[0][n] + minimumPath(cost, 0, n-1)

    # 2. This is the first column of cost matrix.
    if n == 0:
        return cost[m][0] + minimumPath(cost, m-1, 0)

    fromTop = cost[m][n] + minimumPath(cost, m-1, n)
    fromLeft = cost[m][n] + minimumPath(cost, m, n-1)
    return min(fromTop, fromLeft)

print('Minimum sum path from using recursion is: {}'.format(minimumPath(cost, 2, 3)))

# Top Down Approach using memoization
# -------------------------------------------------------------

m = len(cost)
n = len(cost[0])
# initialize all values of memo to zero
memo = [[0 for i in range(n)] for i in range(m)]

def minimumCostTopDown(cost, m, n):

    # base condition
    if m == 0 and n == 0:
        ans = cost[0][0]
        memo[0][0] = ans
        return ans

    if memo[m][n] != 0:
        return memo[m][n]

    # boundry conditions
    # 1. This is the first row
    if m == 0:
        ans = cost[0][n] + minimumCostTopDown(cost, 0, n-1)

    # 2. This is the first column
    elif n == 0:
        ans = cost[m][0] + minimumCostTopDown(cost, m-1, 0)

    else:
        fromTop = cost[m][n] + minimumCostTopDown(cost, m-1, n)
        fromLeft = cost[m][n] + minimumCostTopDown(cost, m, n-1)
        ans = min(fromLeft, fromTop)

    # save the answer to memo before returning
    memo[m][n] = ans
    return ans

print('Minimum sum path using Top Down Approach with Memoization is: {}'.format(minimumCostTopDown(cost, 2, 3)))

# Bottom Up Dynamic Programming
# -------------------------------------------------------
m = len(cost)
n = len(cost[0])
memo = [[0 for i in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):

        if i == 0 and j == 0:
            memo[0][0] = cost[0][0]

        if i == 0:
            # first row
            memo[i][j] = memo[i][j-1] + cost[i][j]

        elif j == 0:
            # first column
            memo[i][j] = memo[i-1][j] + cost[i][j]

        else:
            fromTop = cost[i][j] + memo[i-1][j]
            fromLeft = cost[i][j] + memo[i][j-1]
            memo[i][j] = min(fromTop, fromLeft)

print('Minimum sum path using Bottom Up Dynamic Programming: {}'.format(memo[m-1][n-1]))
