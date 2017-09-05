# Given two words A and B, find the minimum number of steps required to convert A to B.
# (Each operation is counted as 1 step.)

# You have following three operations permitted on a word.
# -Delete a character
# -Insert a character
# -Replace a character

# Example:
# Edit distance between "Anshuman" and "Antihuman" is 2.
# Operation 1: replace s with t
# Operation 2: insert i

# Recursive approach:
# ----------------------------------------------

def editDist(A, B):

    # base condition:
    if not A and not B:
        return 0

    # boundary conditions
    # 1. String A is empty and B is not empty
    if not A and B:
        return len(B)

    # 2. String B is empty and A is not empty
    if not B and A:
        return len(A)

    if A[0] == B[0]:
        return editDist(A[1:], B[1:])

    else:
        # delete first character of A and check editDist
        delete = editDist(A[1:], B)
        # insert the character in A to match and check editDist of rest
        insert = editDist(A, B[1:])
        # replace the first character of A to match and check editDist
        replace = editDist(A[1:], B[1:])

        return 1 + min(delete, insert, replace)

# Bottom up Dynamic Programming:
# ---------------------------------------------

#Use edit dist table
def edit_Distance_DP(A, B):
    m = len(A)
    n = len(B)
    edits = [[0 for i in range(m+1)] for i in range(n+1)]

    # initialize first row
    for i in range(m+1):
        edits[0][i] = i

    # initialize first column
    for i in range(1, n+1):
        edits[i][0] = i


    for i in range(1, n+1):
        for j in range(1, m+1):
            # if the characters match
            if A[j-1] == B[i-1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                delete = edits[i-1][j]
                insert = edits[i][j-1]
                replace = edits[i-1][j-1]
                edits[i][j] = 1 + min(delete, insert, replace)

    #print(edits)
    return edits[n][m]

A = 'saturday'
B = 'sunday'
print('Edit distance of "{}" and "{}" is: {}'.format(A, B, editDist(A, B)))
print('Edit distance of "{}" and "{}" using Dynamic Programming is: {}'.format(A, B, edit_Distance_DP(A, B)))
