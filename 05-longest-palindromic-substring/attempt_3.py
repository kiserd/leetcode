# Author: Donald Logan Kiser
# Date: 08/14/2021
# Problem: leetcode #5 longest palindromic substring
# Description: initial attempt would timeout on long strings. plan to utilize
#              discussion hints to improve efficiency

#              saw a solution in the discussion that does not appear to use
#              dynamic programming (or any memoization or helper arrays of any
#              sort). Giving it a shot from memory to help understand its
#              power.

#              saw a clever use of max using string length to cut down on
#              branching logic. Reverted back to long winded solution, because
#              it did not help with time

class Solution:
    def longestPalindrome(self, s):
        length = 1
        substring = s[0]
        # loop through matrix
        for i in range(len(s)):
            max_new = ''
            new1 = self.helper(s, i, i)
            new2 = self.helper(s, i, i + 1)
            # substring = max([substring, new1, new2], key=lambda x, :len(x))
            if len(new1) > len(new2):
                max_new = new1
            else:
                max_new = new2
            if len(max_new) > length:
                substring = max_new
                length = len(max_new)
        return substring
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

 