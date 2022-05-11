class Solution:
    def combinationSum3(self, k: int, n: int):
        # define recursive helper function
        def dp(num, count, target):
            # handle base case
            if count == k and target == 0:
                return [[]]
            # handle recursive exploration
            res = []
            for i in range(num, 10):
                for combo in dp(i + 1, count + 1, target - i):
                    res.append([i] + combo)
            return res
        # kick off function
        return dp(1, 0, n)
