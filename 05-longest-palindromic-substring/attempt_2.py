# Author: Donald Logan Kiser
# Date: 08/14/2021
# Problem: leetcode #5 longest palindromic substring
# Description: initial attempt would timeout on long strings. plan to utilize
#              discussion hints to improve efficiency

#              pre-populating the 2d array with False and removing that branch
#              from the code manifested in it finishing with a poor score

#              decided to pre-populate the 2d array with True for single
#              element substrings. Had removed this originally

#              decided to condense branches that handled substrings of length
#              2 and checking bookend elements for equality and middle
#              substring for palindrome property

class Solution:
    def longestPalindrome(self, s):
        # bool at A[i, j] indicates whether the string beginning at index i and
        # ending at index j is a palindrome
        A = [[False for i in range(len(s))] for i in range(len(s))]
        length = 1
        substring = s[0][0]
        # pre-populate single length string 2d array values
        for i in range(len(s)):
            A[i][i] = True
        # loop through matrix
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s), 1):
                if j - i < 2 or A[i + 1][j - 1]:
                    A[i][j] = s[i] == s[j]
                if A[i][j] and j - i + 1 > length:
                    length = j - i + 1
                    substring = s[i:j+1]
        return substring
 