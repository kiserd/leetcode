# bottom-up
class Solution:
    def change(self, amount: int, coins) -> int:
        # build memo and set base case implicitly
        memo = [[0] * (amount + 1) for i in range(len(coins) + 1)]
        for i in range(len(coins)):
            memo[i][0] = 1
        # for i in range(amount + 1):
        #     memo[0][i] = 0
        # build memo from base case up
        for i in range(0, len(coins), 1):
            for j in range(1, amount + 1, 1):
                # print('memo: ', memo)
                if j - coins[i] >= 0:
                    memo[i][j] = memo[i][j - coins[i]] + memo[i - 1][j]
                else:
                    memo[i][j] = memo[i - 1][j]
        return memo[len(coins) - 1][amount]