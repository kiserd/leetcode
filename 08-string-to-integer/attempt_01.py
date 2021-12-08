# Author: Donald Logan Kiser
# Date: 08/12/2021
# Description: first attempt at the problem. Intentionally not 'over-thinking'
#              things. Just trying to get familiar with the problem via dumb
#              blind tinkering.
#
#              given len(nums1) = n and len(nums2), this solution will most
#              likely be O(m+n) at best

class Solution:
    def myAtoi(self, s):
        # handle case where string input is empty
        if len(s) == 0:
            return 0
        # create a couple helper variables
        validNums = '0123456789'
        sign = 1
        num = 0
        index = 0
        # strip whitespace
        s = s.strip()
        # check for indication of negative number
        if index < len(s) and s[index] == '-':
            sign = -1
            index += 1
        elif index < len(s) and s[index] == '+':
            index += 1
        # iterate through elements in string
        while index < len(s) and s[index] in validNums:
            num = (num * 10) + (ord(s[index]) - 48)
            index += 1
        # return to user or calling function
        return max(-2**31, min(sign * num, 2**31 - 1))

