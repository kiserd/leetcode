# working through problem from intuition
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [None] * (len(s) + 1)
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            elif s[i] == '1' or (s[i] == '2' and -1 < int(s[i + 1]) < 7):
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        print('dp: ', dp)
        return dp[0]