class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_POS = (2**31) - 1
        MIN_NEG = -(2**31)
        # remove whitespace
        i = 0
        s = s.strip(' ')
        # handle edge case
        if not s: return 0
        # determine sign and potentially increment pointer
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        # isolate digits
        i = 0
        while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
            i += 1
        s = s[:i]
        # remove leading zeros
        i = 0
        while i < len(s) and s[i] == '0':
            i += 1
        if s == len(s): return 0
        s = s[i:]
        # convert string number into integer
        j = 0
        num = 0
        while j < len(s):
            if num > MAX_POS // 10:
                if sign == 1: return MAX_POS
                else: return MIN_NEG
            if num == MAX_POS // 10 and MAX_POS % 10 < ord(s[j]) % ord('0'):
                if sign == 1: return MAX_POS
                else: return MIN_NEG
            num *= 10
            num += (ord(s[j]) % ord('0'))
            j += 1
        return num * sign
