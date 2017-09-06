# String C is aid to be interleaving of string A and B if it contains all the characters
# of A and B and the relative order of characters of both the strings is preserved in C.

# for example if A = xyz and B = abcd and C = axbyczd then
# string C is interleaving of string A and string B

# Given String A, B, and C. Write a function to check if C is interleaving of A and B or not.

# Recursive Approach:
# --------------------------------------------------

def intervleaving(A, B, C):
    if len(A) + len(B) != len(C):
        return False

    if not A and not B and not C:
        return True

    if not A and not B and C:
        return False

    if A and B and not C:
        return False

    #print (A, B, C)
    fromA, fromB = False, False
    if A and A[0] == C[0]:
        fromA = intervleaving(A[1:], B, C[1:])

    if B  and B[0] == C[0]:
        fromB = intervleaving(A, B[1:], C[1:])

    return fromA or fromB

# Dynamic Programming
# ------------------------------------------------------

def interleaving_dp(A, B, C):
    m = len(A)
    n = len(B)
    o = len(C)

    if m + n != o:
        return False

    # create a (n+1)X(m+1) matrix
    inter = [[0 for i in range(m+1)] for i in range(n+1)]

    # Base condition
    # both the strings are empty
    inter[0][0] = 1

    # Boundry condition
    # for first row
    for i in range(1, m+1):
        if A[i-1] != C[i-1]:
            inter[0][i] = 0
        else:
            inter[0][i] = inter[0][i-1]

    # for first column
    for i in range(1, n+1):
        if B[i-1] != C[i-1]:
            inter[i][0] = 0
        else:
            inter[i][0] = inter[i-1][0]

    for i in range(1, n+1):
        for j in range(1, m+1):
            x = A[j-1] # current character of A
            y = B[i-1] # current character of B
            z = C[i+j-1] # current character of C

            # print('A:{}, B:{}, C:{}'.format(x, y, z))
            # if current character of C doens't match with
            # character of A and character of B
            if x != z and y != z:
                inter[i][j] = 0

            # if current character of C matches with character of A
            # but not with current chracter of B
            elif x == z and y != z:
                # take left cell
                inter[i][j] = inter[i][j-1]

            # if current character of C matches with character of B
            # but not with current character of A
            elif x != z and y == z:
                # take upper cell
                inter[i][j] = inter[i-1][j]

            # if current character of C matches with
            # both the character of A and character of B
            elif x ==z and y == z:
                # take logical OR of upper and left cells
                inter[i][j] = inter[i-1][j] or inter[i][j-1]

    #print(inter)
    return inter[n][m]




A = 'bbca'
B = 'bcc'
C = 'bbcbcac'

print('Using Recursion:')
if intervleaving(A, B, C):
    print('{} is interleaving of {} and {}'.format(C, A, B))
else:
    print('{} is not interleaving of {} and {}'.format(C, A, B))

print('Using Dynamic Programming:')
if interleaving_dp(A, B, C):
    print('{} is interleaving of {} and {}'.format(C, A, B))
else:
    print('{} is not interleaving of {} and {}'.format(C, A, B))


