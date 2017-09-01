# Permutations. [No Duplicates]
# Given a collection of numbers, return all possible permutations.
# Example:
# [1,2,3] will have the following permutations:

# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]

# NOTE:
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.

# @param current   : holds the current permutation
# @param remaining : holds the remaining items to be added in current permutation
# @param solution  : holds the all possible permutation found
# returns the solution list
def permute(current, remaining, solution):

    # base condition
    if not remaining:
        solution.append(current[:])
        return solution

    # if items in remaining list
    for i in range(len(remaining)):
        item = remaining[i]
        current.append(item)
        remaining.remove(item)
        solution = permute(current, remaining, solution)
        current.pop()
        remaining.insert(i, item)

    return solution


def main():
    A = [1, 2, 3]
    remaining = A
    current = []
    solution = []

    solution = permute(current, remaining, solution)

    for permutation in solution:
        print(permutation)

if __name__ == '__main__':
    main()
