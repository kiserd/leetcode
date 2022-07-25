class Solution:
    def generateParenthesis(self, n: int):
        # define recursive helper function
        def rec(left, right):
            # handle base case
            if left == n:
                return [')' * (n - right)]
            # handle recursive exploration
            res = []
            for combo in rec(left + 1, right):
                res.append('(' + combo)
            if left > right:
                for combo in rec(left, right + 1):
                    res.append(')' + combo)
            return res
        # kick off recursive helper function
        return rec(0, 0)
