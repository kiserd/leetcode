class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        n = len(nums)
        # get the array of maximum right sums
        rt_sum = nums[n - 1]
        max_rt = [None] * n
        max_rt[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rt_sum += nums[i]
            max_rt[i] = max(max_rt[i + 1], rt_sum)
        # get the greatest single interval subarray
        max_sum = -30001
        prev = -30001
        for i in range(n):
            prev = max(nums[i], nums[i] + prev)
            max_sum = max(max_sum, prev)
        # get the greatest two-interval subarray
        left_sum = 0
        for i in range(n - 2):
            left_sum += nums[i]
            if nums[i] > 0:
                max_sum = max(max_sum, left_sum + max_rt[i + 2])
        return max_sum
