class Solution:
    def jump(self, nums) -> int:
        current = 0
        reach = 0
        jumps = 0
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if i == current:
                jumps += 1
                current = reach
                if reach >= len(nums) - 1: return jumps
        return jumps
            