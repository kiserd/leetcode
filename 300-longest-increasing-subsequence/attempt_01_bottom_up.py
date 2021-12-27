# bottom-up
class Solution:
    def lengthOfLIS(self, nums) -> int:
        # build memo array
        memo = [None] * len(nums)
        memo[0] = 1
        # iterate through possible ending indices, populating memo
        for i in range(1, len(nums), 1):
            max_lcs = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    max_lcs = max(max_lcs, memo[j] + 1)
            memo[i] = max_lcs
        # return memoized result for last index
        return max(memo)
