class Solution:
    def letterCombinations(self, digits):
        # handle edge case
        if digits == '': return []
        # build map
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # define recursive helper function
        def rec(i):
            # handle base case
            if i == len(digits):
                return ['']
            # handle recursive exploration
            res = []
            for char in map[digits[i]]:
                for combo in rec(i + 1):
                    res.append(char + combo)
            return res
        # kick off recursive helper function
        return rec(0)