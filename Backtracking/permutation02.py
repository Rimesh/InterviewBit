# permutation02.py [with Duplicates
def main():
    A = 'abbc'
    n = len(A)
    items, counts = getCount(A)
    solutions = []
    window = []
    level = 0
    solutions = findPermutations(items, counts, window, solutions, level, n)

    for permutation in solutions:
        print(permutation)

# returns all permutations in lexicographical order
def findPermutations(items, counts, window, solutions, level, n):

    # base case
    if level == n:
        solutions.append(window[:])
        return solutions

    for i in range(len(counts)):
        if counts[i] == 0:
            continue

        counts[i] -= 1
        window.append(items[i])
        findPermutations(items, counts, window, solutions, level+1, n)
        window.pop()
        counts[i] += 1

    return solutions

def getCount(A):
    itemcount = dict()
    for item in A:
        if itemcount.get(item, 0) == 0:
            itemcount[item] = 1
        else:
            itemcount[item] += 1
    items = list((itemcount.keys()))
    items.sort()
    counts = [itemcount[item] for item in items]
    return items, counts

if __name__ == '__main__':
    main()
