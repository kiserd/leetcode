# Author: Donald Logan Kiser
# Date: 08/12/2021
# Problem: leetcode #20 valid parentheses
# Description: second attempt at problem after glancing at clever solutions
#              in discussion

#              used neat little quick check for odd # of elements

#              tinkered around a bit with reversing the order of the keys
#              and values in my dict. The operations on the built-in data
#              structure might be less expensive (this did not appear to have
#              a beneficial impact)

#              tried really cool trick to remove the need to check whether the
#              stack is empty before popping by including a 'head' element

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        brackets = {"h": "h", "(": ")", "{": "}", "[": "]"}
        stack = ['h']
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            else:
                if c!= brackets[stack.pop()]:
                    return False
        return stack == ["h"]
