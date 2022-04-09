class Solution:
    def combine(self, n: int, k: int):
        # define backtracking function
        def backtrack(num, count):
            """ works through range of nums populating combination arrays"""
            # handle base case(s)
            if n - num + 1 < k - count:
                return False, None
            if count == k:
                return True, [[]]
            # handle recursive case
            res = []
            for i in range(num, n + 1):
                valid, combos = backtrack(i + 1, count + 1)
                if valid:
                    for combo in combos:
                        res.append([i] + combo)
            # handle case where recursive search rendered invalid result
            if not res:
                return False, None
            # return combinations and valid indication to calling function
            return True, res
        # kick off function
        return backtrack(1, 0)[1]
