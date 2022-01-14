# date: 01/13/2022
class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = ''
        # check palindromes that start with one char
        for i in range(len(s)):
            # work from inside out
            m = i
            n = i
            count = 1
            while m - 1 > -1 and n + 1 < len(s) and s[m - 1] == s[n + 1]:
                count += 2
                m -= 1
                n += 1
            if count > len(curr):
                curr = s[m:n + 1]
        # check palindromes that start with two chars
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                m = i - 1
                n = i
                count = 2
                while m - 1 > -1 and n + 1 < len(s) and s[m - 1] == s[n + 1]:
                    count += 2
                    m -= 1
                    n += 1
                if count > len(curr):
                    curr = s[m:n + 1]
        return curr


# dynamic programming feels like my knee-jerk response