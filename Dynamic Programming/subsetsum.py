# Given an array of non negative intergers and a positive number X ,
# determine if there exist a subset of elements of array with sum = X.

# Example:
# input: {3, 2, 7, 1}  X = 6
# output: True # because sum of (3, 2, 1) is 6

# Recusrsive approach:
# ----------------------------------------------------

def isSubsetSum(A, x):
    # base condition:
    if x == 0:
        return True

    # if no elements in array:
    if len(A) == 0:
        return False

    # if first element is greater than X, skip it
    current = A[0]
    if current > x:
        return isSubsetSum(A[1:], x)

    # two possibilities
    # either include the first elemet or exclude the first element
    include = isSubsetSum(A[1:], x-current)
    exclude = isSubsetSum(A[1:], x)
    return include or exclude

# Dynamic approach
# --------------------------------------------------
def isSubsetSum_DP(A, x):
    n = len(A)
    subset = [[False for i in range(x+1)] for i in range(n)]

    # base case
    # first column is sum 0: all Are True
    for i in range(n):
        subset[i][0] = True

    #fill the first row
    for i in range(1, x+1):
        if i != A[0]:
            continue
        else:
            subset[0][i] = True

    # fill rest of the cells
    for i in range(1, n):
        for j in range(1, x+1):
            value = A[i]
            # copy the previous row for lesser value subsets
            if j < value:
                subset[i][j] = subset[i-1][j]
            elif j == value: # if value == sum
                subset[i][j] = True
            elif subset[i-1][j] == True: # if previous subset is True
                subset[i][j] = True
            else: # try adding value to subset and check
                subset[i][j] = subset[i-1][j-value]

    #print(subset)
    return subset[n-1][x]

# Driver program
# ------------------------------------------------------

A = [3, 2, 7, 1]
X = 6

print('By Recusrsion:')
if isSubsetSum(A, X):
    print('There is a subset with sum : {}'.format(X))
else:
    print('There is no subset with sum : {}'.format(X))

print('By Dynamic programming:')
if isSubsetSum_DP(A, X):
    print('There is a subset with sum : {}'.format(X))
else:
    print('There is no subset with sum : {}'.format(X))
