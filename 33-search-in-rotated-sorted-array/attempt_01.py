class Solution:
    def search(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high - low) // 2
        while low <= high:
            # handle case of hit
            if nums[mid] == target:
                return mid
            # handle case where mid is greater
            if nums[mid] > target:
                # handle case where num is between mid and high
                if nums[mid] > nums[high] and nums[high] >= target:
                    low = mid + 1
                # handle case where num is between low and mid
                # this is a lot like normal binary search
                # captures:
                # nums[mid] < nums[high]
                # or
                # nums[high] < target
                else :
                    high = mid - 1
            elif nums[mid] < target:
                # handle case where num is between low and mid
                if nums[mid] < nums[low] and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            mid = low + ((high - low) // 2)
        return - 1