class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        res = ''
        def lp(i, j):
            # handle case of initial non-equals
            if s[i] != s[j]:
                return ''
            # test from middle out
            while i > -1 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    return s[i + 1:j]
            return s[i + 1: j]
        for idx in range(1, len(s)):
            # check single elt origin
            res = max(res, lp(idx, idx), lp(idx - 1, idx), key=lambda x: len(x))
        return res
