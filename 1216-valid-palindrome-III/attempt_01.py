class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # build memo array
        memo = [[None] * len(s) for _ in range(len(s))]

        # define recursive helper function
        def dp(l, r):
            # handle base case
            if r <= l:
                memo[l][r] = 0
                return memo[l][r]
            # handle recursive exploration
            if memo[l][r] is None:
                if s[l] == s[r]:
                    memo[l][r] = dp(l + 1, r - 1)
                else:
                    memo[l][r] = 1 + min(dp(l + 1, r), dp(l, r - 1))
            return memo[l][r]

        return dp(0, len(s) - 1) <= k
