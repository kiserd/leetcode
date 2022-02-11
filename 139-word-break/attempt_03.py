# returning to solve via intuition
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # get max word length from wordDict
        max_word = 0
        for word in wordDict:
            max_word = max(max_word, len(word))
        # build recursive function
        def dp(i):
            # handle base case
            if s[i:] in wordDict:
                return True
            # handle recursive exploration
            if memo[i] is None:
                j = 1
                while i + j < len(s) and j <= max_word:
                    if s[i: i + j] in wordDict:
                        if dp(i + j): return True
                    j += 1
                memo[i] = False
            return memo[i]
        # build memo array
        memo = [None] * len(s)
        return dp(0)