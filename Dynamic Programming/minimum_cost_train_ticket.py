
# There are N stations in a route, starting from 0 to N-1.
# A train moves from first station (0) to last station (N-1) in only forward direction.
# The cost of ticket between any two station is given, find the minimum cost to travel
# from station 0 to N-1

# cost matrix
cost = [[ 0, 10, 75, 94],
        [-1,  0, 35, 50],
        [-1, -1,  0, 80],
        [-1, -1, -1,  0]]

# solution using recursion
def minCost(s, d):
    # base condition
    if s == d:
        return 0

    # if source and destination are next to each other
    if s == d-1:
        return cost[s][d]

    # let minimumCost be the cost from source to destination
    minimumCost = cost[s][d]

    # try to break at every station in between and check if we can get minimum cost
    for i in range(s+1, d):
        temp = minCost(s, i) + minCost(i, d)
        if temp < minimumCost:
            minimumCost = temp

    return minimumCost

print('Minimum Cost using recursion: ', minCost(0, 3))

# Top Down - Memoized solution
# ----------------------------------------------------------

# store the minimum cost for each station in a memo
# required solution will be memo[n-1]

# since there are 4 stations create a memo of size 4
# initialize it with 0, it means mincost is not available
memo = [[0]*4 for x in range(4)]

def memoizedMinCost(s, d):
    # base condition
    if (s == d) or (s == d-1):
        return cost[s][d]

    # if mincost is not found in memo:
    if memo[s][d] == 0:

        minimumCost = cost[s][d]

        # try to find the cost for inbetween stations
        for i in range(s+1, d):

            temp = memoizedMinCost(s, i) + memoizedMinCost(i, d)
            if temp < minimumCost:
                minimumCost = temp

        # update the memo
        memo[s][d] = minimumCost

    return memo[s][d]

print('Minimum Cost using Memoized Top Down approach: ', memoizedMinCost(0, 3))

# Bottom - Up Dynamic Programming
# ---------------------------------------------

# The approach is to first calculate minimum cost for station 0
# then station 1 and so on... station N-1

# Minimum cost of station 0 is 0, because we are already there
# mincost[0] = 0

# Minimum cost of station 1 is cost[0][1] since they are next to each other
# mincost[1] = cost[0][1]

# Minimum cost of station 2 is minimum of
# 1. mincost[0] + cost[0][2]
# 2. mincost[1] + cost[1][2]

def bottomUpMinCost(cost):
    # cost is N*N matrix
    n = len(cost)

    # mincost[i] is minimum cost from station 0 to station i
    mincost = [None]*n
    mincost[0] = 0
    mincost[1] = cost[0][1]

    for i in range(2, n):
        mincost[i] = cost[0][i]

        for j in range(1, i):
            if mincost[i] > mincost[j] + cost[j][i]:
                mincost[i] = mincost[j] + cost[j][i]

    return mincost[n-1]

print('Minimum Cost using BottomUp Dynamic Programming approach: ', bottomUpMinCost(cost))
