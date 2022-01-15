class Solution:
    def lengthOfLIS(self, nums) -> int:
        # define memo array
        dp = [1] * len(nums)
        # build memo array from bottom up
        for i in range(1, len(nums)):
            new = 1
            # loop back through elements prior to i
            for j in range(i - 1, -1, -1):
                # if current element is greater, append element to that subseq
                if nums[i] > nums[j]:
                    # if this represents a new max LIS, update var
                    if 1 + dp[j] > new:
                        new = 1 + dp[j]
            dp[i] = new
        return max(dp)

# dp[i] represents the longest subsequence ending on and including index i