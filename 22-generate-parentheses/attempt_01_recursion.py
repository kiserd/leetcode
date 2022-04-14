class Solution:
    def generateParenthesis(self, n: int):
        # define recursive function
        def helper(s, left, right):
            # handle base case
            if len(s) == 2 * n:
                res.append(s)
            # handle recursive exploration
            else:
                if left < n:
                    helper(s + '(', left + 1, right)
                if right < left:
                    helper(s + ')', left, right + 1)
        # setup return vessel and call function
        res = []
        helper('(', 1, 0)
        return res
