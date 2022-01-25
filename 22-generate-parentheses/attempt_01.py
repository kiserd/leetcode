class Solution:
    def generateParenthesis(self, n: int):
        # define recursive function
        def gen(n):
            # handle base case
            if n == 1: return ['()']
            # handle recursive exploration
            rec = gen(n - 1)
            left = ['()' + elt for elt in rec]
            mid = ['(' + elt + ')' for elt in rec]
            right = [ elt + '()' for elt in rec]
            return left + mid + right
        return list(set(gen(n)))
