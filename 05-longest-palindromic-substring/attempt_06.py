class Solution:
    def longestPalindrome(self, s: str) -> str:
        # handle edge case, maybe return early
        if len(s) == 1: return s[0]
        # define function to determine longest palindrome built around indices
        def get_pal(i, j):
            if s[i] == s[j]:
                while i - 1 >= 0 and j + 1 < len(s) and s[i - 1] == s[j + 1]:
                    i -= 1
                    j += 1
                return s[i:j + 1]
            return s[i]
        # process array from potential midpoints
        res = s[0]
        for i in range(len(s) - 1):
            sgl = get_pal(i, i)
            dbl = get_pal(i, i + 1)
            res = max(res, sgl, dbl, key=lambda x: len(x))
        return res
