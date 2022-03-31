class Solution:
    def getRow(self, rowIndex: int):
        # build recursive function
        def dp(i, j):
            # handle base case
            if j == 0 or j == i:
                return 1
            # handle recursive case
            if not memo.get((i, j), False):
                memo[(i, j)] = dp(i - 1, j - 1) + dp(i - 1, j)
            return memo[(i, j)]
        # build memo array
        memo = {}
        res = [None] * (rowIndex + 1)
        for col in range(len(res)):
            res[col] = dp(rowIndex, col)
        return res
