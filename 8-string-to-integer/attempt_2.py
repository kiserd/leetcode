# Author: Donald Logan Kiser
# Date: 08/12/2021
# Description: second attempt at problem after glancing at clever techniques
#              used in discussion

class Solution:
    def myAtoi(self, s):
        arr = list(s.strip())
        if len(arr) == 0:
            return 0
        sign = 1
        num = 0
        index = 0
        if arr[index] == '-':
            sign = -1
            index += 1
        elif arr[index] == '+':
            index += 1
        while index < len(arr) and arr[index].isdigit():
            num = (num * 10) + (ord(arr[index]) - 48)
            index += 1
        return max(-2**31, min(sign * num, 2**31 - 1))

