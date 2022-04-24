class Solution:
    def permuteUnique(self, nums):
        # build array of counts
        counts = [0] * 21
        for num in nums:
            counts[num + 10] += 1

        # define recursive helper function
        def rec(arr, off_limits):
            # handle base case
            if arr == [0] * 21:
                return [[]]
            # handle recursive case
            res = []
            for i, count in enumerate(arr):
                if i != off_limits and arr[i]:
                    for j in range(1, arr[i] + 1):
                        arr[i] -= j
                        for perm in rec(arr, i):
                            res.append([i - 10 for _ in range(j)] + perm)
                        arr[i] += j
            return res

        return rec(counts, -1)
