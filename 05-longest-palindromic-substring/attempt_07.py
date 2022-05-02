class Solution:
    def longestPalindrome(self, s: str) -> str:
        # handle edge case
        if len(s) == 1:
            return s
       # define helper function
        def get_pal(i, j):
            while i > -1 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        # iterate through all possible palindrome "starts"
        res = ''
        for idx in range(1, len(s)):
            # get longest palindrome originating from single char
            single_start = get_pal(idx, idx)
            # get longest palindrome originating from two chars
            double_start = ''
            if s[idx] == s[idx - 1]:
                double_start = get_pal(idx - 1, idx)
            # update res if applicable
            res = max(res, single_start, double_start, key=lambda x: len(x))
        return res
