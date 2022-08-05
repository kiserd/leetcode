class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # init memo array
        memo = [[None] * len(text2) for _ in range(len(text1))]

        # define recursive function
        def dp(i, j):
            # handle base case
            if i < 0 or j < 0:
                return 0
            # handle recursive exploration
            if memo[i][j] is None:
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + dp(i - 1, j - 1)
                else:
                    memo[i][j] = max(dp(i - 1, j), dp(i, j - 1))
            return memo[i][j]
        # kick off recursive function
        return dp(len(text1) - 1, len(text2) - 1)
