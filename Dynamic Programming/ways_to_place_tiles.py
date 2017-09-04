# Given an empty plot of size 3 x n.
# we want to place tiles such that the entire plot is covered.
# Each tile is of size 2 x 1 and can be placed either vertically or horizontally.

#  vertically : ||    horizontal : ====
#               ||

# Write a function that accepts n as input and return the total number of ways in which
# we can place the tiles(without breaking any tile).

# Resursive approach
# --------------------------------------------------

# if n == 2, we can place tile in 3 possible ways

# || ||    and    ====   and    ====
# || ||           || ||         ====
#  ====           || ||         ====

# n == 4, we can place tiles in 9 possible ways..

def place_tiles(n):

    # if n is not multiple of 2,
    # The plot cannot be fully covered by 2X1 tile
    if n%2 != 0 or n <= 0:
        return 0

    if n >= 4:
        return 9 + place_tiles(n-4)
    else:
        # n == 2
        return 3 + place_tiles(n-2)

print('Ways to place tile: {}'.format(place_tiles(12)))

# using iteration:
# ------------------------------------------------------

def place_tiles_iteration(n):
    ways = 0

    if n%2 != 0:
        return 0

    while n >= 4:
        ways += 9
        n -= 4

    if n == 2:
        ways += 3

    return ways

print('Ways to place tiles: {}'.format(place_tiles_iteration(12)))


