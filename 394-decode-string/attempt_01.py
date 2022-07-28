class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        mult = ''
        for ch in s:
            if ord('a') <= ord(ch) <= ord('z'):
                res += ch
            elif ord('0') <= ord(ch) <= ord('9'):
                mult += ch
            elif ch == '[':
                stack.append((mult, res))
                res = ''
                mult = ''
            elif ch == ']':
                times, prev = stack.pop()
                res *= int(times)
                res = prev + res
        return res
