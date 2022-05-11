class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        # put all nums in arr and sort them
        arrs = [nums1, nums2, nums3, nums4]
        m = len(arrs)
        n = len(arrs[0])
        # define func to build mapping
        memo = {}
        def dp(i, target):
            # handle successful base case
            if i == m:
                if target == 0:
                    return 1
                else:
                    return 0
            # handle recursive exploration
            if (i, target) not in memo:
                res = 0
                for idx in range(n):
                    res += dp(i + 1, target - arrs[i][idx])
                memo[(i, target)] = res
            return memo[(i, target)]
        return dp(0, 0)
