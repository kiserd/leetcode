from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            idx = 0
            while idx < len(wordDict) and dp[i] is None:
                word = wordDict[idx]
                if i - len(word) > - 1:
                    if dp[i - len(word)] and s[i-len(word):i] == word:
                        dp[i] = True
                idx += 1
        return dp[len(s)]
