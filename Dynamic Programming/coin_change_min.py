# Given an infinite suppy of coins of N different denominations (values)
# Find the minimum number of coins that sum upto number k

# recursive approach:
# ---------------------------------------------
import math
def coin_change(coins, k):

    # base condition
    if k == 0:
        return 0

    change = math.inf
    for coin in coins:
        # if coin is greater than sum then skip the coin
        if coin > k:
            continue
        else:
            # try each coin which is smaller than sum
            temp = 1 + coin_change(coins, k-coin)
            if temp < change:
                change = temp

    return change


# Dynamic programming
# -------------------------------------------------------------

def coin_change_dp(coins, k):
    # dp array to save minimum coins for required sum starting 0 till k
    mincoins = [math.inf for i in range(k+1)]
    mincoins[0] = 0 # base case 0 coins needed to make sum 0
    for i in range(1, k+1): # iterate through each sum, bottom up
        for coin in coins:
            if coin <= i: # coins which are lesser than current sum
                temp = 1 + mincoins[i-coin]
                if temp < mincoins[i]:
                    mincoins[i] = temp
    return mincoins[k]



coins = [1, 5, 6, 9]
K = 11

print('Using recursion:')
print('Minimum coins needed to sum {} from coins {} are: {}'.format(K, coins, coin_change(coins, K)))
print('Using Dynamic Programming:')
print('Minimum coins needed to sum {} from coins {} are: {}'.format(K, coins, coin_change_dp(coins, K)))
