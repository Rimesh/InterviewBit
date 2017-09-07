# Given two strings, write a function that returns the total number of characters in their
# Longest Common Subsequence (LCS).
# Additional: Also print the LCS

# Recursive approach:
# --------------------------------------------------

def lcs(A, B):
    m = len(A)
    n = len(B)

    # base condition:
    if m == 0 and n == 0:
        return 0

    # Boundry case:
    if m == 0 or n == 0:
        return 0

    if A[-1] == B[-1]:
        return 1 + lcs(A[:-1], B[:-1])
    else:
        fromA = lcs(A[:-1], B)
        fromB = lcs(A, B[:-1])
        return max(fromA, fromB)


# Dynamic programming:
# ---------------------------------------------

def lsc_dynamic(A, B):
    m = len(A)
    n = len(B)

    if m == 0 or n == 0:
        return 0

    # create a 2d matrix to store intermediate result
    # add one more dimension for comparing empty strings
    # string A is taken horizontally
    # string B is taken vertically
    lcs = [[0 for i in range(m+1)] for i in range(n+1)]

    # initialize boundry case
    # 1. first row
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
                continue

            #print('A:{}, B:{}'.format(A[j-1] , B[i-1]))
            if A[j-1] == B[i-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                # if left cell is greater than upper cell
                if lcs[i][j-1] > lcs[i-1][j]:
                    lcs[i][j] = lcs[i][j-1]
                else:
                    lcs[i][j] = lcs[i-1][j]
    #print(lcs)
    return lcs

def getLcsString(lcs_matrix, A, B):
    n = len(lcs_matrix) # rows
    m = len(lcs_matrix[0]) # columns
    lcs_string = ''
    # string A is taken horizontally in matrix
    # string B is taken vertically in matrix

    i = n-1
    j = m-1

    while i > 0  and j > 0:
            if A[j-1] == B[i-1]:
                lcs_string = A[j-1] + lcs_string
                i -= 1
                j -= 1
            else:
                # different characters
                # if left cell is
                if lcs_matrix[i][j-1] > lcs_matrix[i-1][j]:
                    j -= 1
                else:
                    i -= 1
    return lcs_string




# Driver program
# ----------------------------------------------
A = 'ACBDF'
B = 'ABCDEF'
print('Using Recursion:')
print('Longest Common Subsequence Length: {}'.format(lcs(A, B)))
print('Using Dynamic Programming:')
lcs_matrix = lsc_dynamic(A, B)
lcs_string = getLcsString(lcs_matrix, A, B)
print('Longest Common Subsequence Length: {}'.format(lcs_matrix[-1][-1]))
print('Longest Common Subsequence String: {}'.format(lcs_string))
