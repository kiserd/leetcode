class Solution:
    def generateParenthesis(self, n: int):
        # use stack to explore possible combinations
        res = []
        stack = [('(', 1, 0)]
        while stack:
            curr, left, right = stack.pop()
            # handle case where only can add right paren(s)
            if left == n:
                res.append(curr + (')' * (n - right)))
            else:
                stack.append((curr + '(', left + 1, right))
                # handle case where right paren possible
                if left > right:
                    stack.append((curr + ')', left, right + 1))
        return res