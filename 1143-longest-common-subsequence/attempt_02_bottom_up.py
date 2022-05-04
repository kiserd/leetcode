class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # iterate through arrays from back to front
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # handle case of equal chars
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # handle case of unequal chars
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        for row in dp:
            print(row)
        return dp[0][0]
