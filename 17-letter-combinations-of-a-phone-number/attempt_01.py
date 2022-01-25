# naive solution
class Solution:
    def letterCombinations(self, digits: str):
        # handle base case
        if len(digits) == 0:
            return []
        dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def gen_combos(digs):
            # handle base case
            if len(digs) == 1:
                return [char for char in dict[digs[0]]]
            # handle recursive exploration
            sub = gen_combos(digs[1:])
            return [num + elt for num in dict[digs[0]] for elt in sub]
        return gen_combos(digits)