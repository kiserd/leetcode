class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # build memo array
        memo = [[None] * len(text2) for _ in range(len(text1))]
        # define recursive helper function
        def dp(i, j):
            # handle base case
            if i == len(text1) or j == len(text2):
                return 0
            # handle recursive exploration
            if memo[i][j] is None:
                # handle case of matching chars
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + dp(i + 1, j + 1)
                else:
                    memo[i][j] = max(dp(i + 1, j), dp(i, j + 1))
            return memo[i][j]
        # kick off function and return result
        return dp(0, 0)
