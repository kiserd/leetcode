# date: 01/13/2022
# combine into single loop
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # handle edge case
        if len(s) == 1:
            return s
        curr = ''
        # check palindromes that start with one char
        for i in range(len(s) - 1):
            sgl = self.get_pal(s, i, i)
            dbl = self.get_pal(s, i, i + 1)
            curr = max([curr, sgl, dbl], key=lambda x: len(x))
        return curr
    
    def get_pal(self, s, i, j):
        if s[i] == s[j]:
            m = i
            n = j
            while m - 1 > -1 and n + 1 < len(s) and s[m - 1] == s[n + 1]:
                m -=1
                n += 1
            return s[m:n + 1]
        return s[i]
