# trying to get a little more clever, use a 1D memo array
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # build recursive dp function
        def dp(i):
            # handle base case where i < 0
            if i < 0:
                return True
            # return memoized result, if available
            if memo[i] is not None:
                return memo[i]
            # no memo available, recursively explore
            else:
                # loop through words in wordDict
                for word in wordDict:
                    n = len(word)
                    # attempt to short-circuit on size and recursively explore substring
                    if n <= i + 1 and dp(i - n):
                        # handle case where both substrings succeed
                        if word == s[i - n + 1: i + 1]:
                            memo[i] = True
                            return True
                # recursive exploration failed, indicate to calling function
                memo[i] = False
                return False
        # build memo and return result of recursive exploration
        memo = [None] * len(s)
        return dp(len(s) - 1)