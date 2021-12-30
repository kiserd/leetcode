# bottom-up
# iterating over coins in the outer-loop is key to not double-counting
# equivalent combinations of coins chosen in different orders. Need to review
# the infinite knapsack problem
class Solution:
    def change(self, amount: int, coins) -> int:
        # build memo and set base case implicitly
        memo = [0] * (amount + 1)
        memo[0] = 1
        for coin in coins:
            for amt in range(1, amount + 1, 1):
                # handle case where current coin can be used
                if coin <= amt:
                    memo[amt] = memo[amt] + memo[amt - coin]
        return memo[amount]