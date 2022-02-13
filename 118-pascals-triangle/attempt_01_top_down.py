class Solution:
    def generate(self, numRows: int):
        # define recursive function
        def dp(i, j):
            # handle recursive exploration
            if not memo[i][j]:
                memo[i][j] = dp(i - 1, j - 1) + dp(i - 1, j)
            return memo[i][j]
        # build memo array with implicit base cases
        memo = [[None] * i for i in range(1, numRows + 1)]
        for i in range(numRows):
            memo[i][0] = memo[i][len(memo[i]) - 1] = 1
        for i in range(1, numRows):
            dp(numRows - 1, i)
        return memo
