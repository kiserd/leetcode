# something in here is wasting some time, but finished without TLE on one
# occasion
from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        # define recursive function
        def dp(n):
            # handle base case(s)
            if memo[n]: return memo[n]
            # handle recursive exploration
            min_count = n
            i = 1
            while i < len(sqs) and sqs[i] <= n:
                count = 1 + dp(n - sqs[i])
                min_count = min(min_count, count)
                i += 1
            memo[n] = min_count
            return min_count
        memo = [None] * (n + 1)
        sqs = [i**2 for i in range(1, int(sqrt(n)) + 1)]
        memo[0] = 0
        return dp(n)


    def isSquare(self, n):
        root = sqrt(n)
        return root - (root // 1) == 0