class Solution:
    def isValid(self, s):
        map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for bracket in s:
            if bracket in map:
                if stack and stack[-1] == map[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack