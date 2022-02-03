# try to clean this up with a sliding window
class Solution:
    def deleteAndEarn(self, nums) -> int:
        # build out helper dict
        helper = {}
        for num in nums:
            helper[num] = helper.get(num, 0) + num
        # build new nums array
        new_nums = sorted([key for key in helper])
        # build out memoization array
        use = 0
        dont = 0
        prev_num = new_nums[0] - 1
        # build memo array from bottom up
        for num in new_nums:
            if num == prev_num + 1:
                use, dont = dont + helper[num], max(use, dont)
            else:
                use, dont = max(use, dont) + helper[num], max(use, dont)
            prev_num = num
        return max(use, dont)
