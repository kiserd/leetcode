from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # define memo array
        memo = [None] * (len(s) + 1)

        # define recursive function
        def dp(i):
            # handle base case
            if i == 0:
                return True
            # handle recursive exploration
            if memo[i] is None:
                for word in wordDict:
                    if s[i - len(word):i] == word:
                        if dp(i - len(word)):
                            memo[i] = True
                            return memo[i]
                memo[i] = False
            return memo[i]
        return dp(len(s))
