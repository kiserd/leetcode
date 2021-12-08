# Author: Donald Logan Kiser
# Date: 08/12/2021
# Problem: leetcode #20 valid parentheses
# Description: first attempt at the problem. Intentionally not 'over-thinking'
#              things. Just trying to get familiar with the problem via dumb
#              blind tinkering.

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        index = 0
        while index < len(s):
            if s[index] in brackets.keys():
                stack.insert(0, s[index])
                index += 1
            else:
                if len(stack) < 1:
                    return False
                elt = stack.pop(0)
                if s[index] != brackets[elt]:
                    return False
                index += 1
        if len(stack) > 0:
            return False
        return True
