from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # init memo array and sort coins
        memo = [None] * (amount + 1)
        coins.sort()

        # define recursive function
        def dp(i):
            # handle base case
            if i == 0:
                return 0
            # handle recursive exploration
            if memo[i] is None:
                idx = 0
                memo[i] = 10001
                while idx < len(coins) and i - coins[idx] > -1:
                    memo[i] = min(memo[i], 1 + dp(i - coins[idx]))
                    idx += 1
            return memo[i]
        res = dp(amount)
        if res > 10000:
            return -1
        return res
