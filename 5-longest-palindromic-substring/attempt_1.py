# Author: Donald Logan Kiser
# Date: 08/13/2021
# Problem: leetcode #5 longest palindromic substring
# Description: first attempt at the problem. Intentionally not 'over-thinking'
#              things. Just trying to get familiar with the problem via dumb
#              blind tinkering.

#              doing my best to recall dp from intro to algorithms with a brief
#              glance at some verbal descriptions of the matrices used

#              experiencing timeouts on long strings, see attempt_2.py

class Solution:
    def longestPalindrome(self, s):
        # bool at A[i, j] indicates whether the string beginning at index i and
        # ending at index j is a palindrome
        A = [[None for i in range(len(s))] for i in range(len(s))]
        length = 0
        substring = ''
        # loop through matrix
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s), 1):
                if j == i:
                    A[i][j] = True
                elif j - i < 2:
                    A[i][j] = s[i] == s[j]
                else:
                    if s[i] != s[j]:
                        A[i][j] = False
                    else:
                        A[i][j] = A[i + 1][j - 1]
                if A[i][j] and j - i + 1 > length:
                    length = j - i + 1
                    substring = s[i:j+1]
        return substring
                
                