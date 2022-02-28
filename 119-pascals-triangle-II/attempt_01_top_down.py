class Solution:
    def getRow(self, rowIndex: int):
        # define recursive function
        def dp(i, j):
            # handle base case
            if j == 0 or j == i:
                return 1
            # handle recursive exploration
            if not memo.get((i, j), False):
                memo[(i, j)] = dp(i - 1, j - 1) + dp(i - 1, j)
            return memo[(i, j)]
        # build memo array
        memo = {}
        res = [None] * (rowIndex + 1)
        res[0] = res[-1] = 1
        for i in range(1, rowIndex):
            res[i] = dp(rowIndex, i)
        return res