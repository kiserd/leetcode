class Solution:
    def isValid(self, s: str) -> bool:
        s = []
        parens = {')': '(', '}': '{', ']': '['}
        op = '({['
        cl = ')}]'
        i = 0
        for paren in s:
            if paren in op:
                s.append(paren)
            else:
                if not s or parens[paren] != s[-1]:
                    return False
                s.pop()
        return not s