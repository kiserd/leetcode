class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        max_reachable = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] == 0 and max_reachable <= idx:
                return False
            max_reachable = max(max_reachable, idx + nums[idx])
            if max_reachable >= len(nums) - 1:
                return True
            idx += 1
        return True

# reduce things to O(n) by knowing that all we care about is hitting 0's, since
# we are returning a boolean indication of success/failure

# track the "max reachable" and when we hit a 0, determine whether we have a
# way of making it past the road block
