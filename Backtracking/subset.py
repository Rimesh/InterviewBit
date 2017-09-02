# Given a set of distinct integers, S, return all possible subsets.
#     Note:
#         Elements in a subset must be in non-descending order.
#         The solution set must not contain duplicate subsets.
#         Also, the subsets should be sorted in ascending ( lexicographic ) order.
#         The list is not necessarily sorted.

# Example :
# If S = [1,2,3], a solution is:
# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]

class Powerset:

    def driver(self, A):
        window = []
        counts = [1]*len(A)
        subsets = []
        subsets = self.subset(A, counts, window, 0, subsets)

        # print subsets:
        for subset in subsets:
            print(subset)

    def subset(self, items, counts, window, position, subsets):
        subsets.append(window[:])
        if position == len(items):
            return subsets

        for i in range(position, len(items)):

            window.append(items[i])
            subsets = self.subset(items, counts, window, i+1, subsets)
            window.pop()
        return subsets

solution1 = Powerset()
solution1.driver([1,2,3])
solution1.driver('ABC')

