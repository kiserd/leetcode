class Solution:
    def search(self, nums, target: int) -> int:
        # define recursive binary search function
        def bin(l, r):
            # handle unsuccessful base case
            if l > r:
                return -1
            # handle successful base case
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            # handle recursive exploration
            if nums[mid] < target:
                if nums[mid] > nums[r] or nums[mid] < target <= nums[r]:
                    return bin(mid + 1, r)
                else:
                    return bin(l, mid - 1)
            else:
                if nums[mid] < nums[l] or nums[mid] > target >= nums[l]:
                    return bin(l, mid - 1)
                else:
                    return bin(mid + 1, r)
        return bin(0, len(nums) - 1)