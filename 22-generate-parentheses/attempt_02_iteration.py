class Solution:
    def generateParenthesis(self, n: int):
        # process using a stack
        # tuple to track things: (current string, left count, right count)
        stack = [('(', 1, 0)]
        res = []
        while stack:
            s, l, r = stack.pop()
            # handle case where final right paren is needed
            if l + r == (2 * n) - 1:
                res.append(s + ')')
            # handle case where we need to add future branches to stack
            else:
                # handle case where left paren is valid
                if l < n:
                    stack.append((s + '(', l + 1, r))
                # handle case where right paren is valid
                if l > r:
                    stack.append((s + ')', l, r + 1))
        return res
