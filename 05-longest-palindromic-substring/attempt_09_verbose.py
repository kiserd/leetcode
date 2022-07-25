class Solution:
    def longestPalindrome(self, s: str) -> str:
        # handle edge case
        if len(s) == 1:
            return s[0]
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
        # process string using helper function
        res = ''
        for idx in range(1, len(s)):
            # get pal from sgl and dbl elt origin
            sgl = lp(idx, idx)
            dbl = lp(idx - 1, idx)
            # update res if applicable
            res = max(res, sgl, dbl, key=lambda x: len(x))
        return res