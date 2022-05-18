# need to seriously dig into this problem, still have a VERY
# loose grasp on the intuition.

# basically need to check for a special case where
# nums[lo] == nums[mid], then proceed with business as usual
# from 33-search-in-rotated...

class Solution:
    def search(self, nums, target: int) -> bool:
        # define recursive search function
        # use recursion due to potentially searching multiple
        # branches
        def bin(lo, hi):
            mid = (lo + hi) // 2
            # handle unsuccessful base case
            if lo > hi:
                return False
            # handle successful base case
            if nums[mid] == target:
                return True
            # handle recursive exploration
            if nums[lo] == nums[mid]:
                return bin(lo, mid - 1) or bin(mid + 1, hi)
            if nums[lo] <= nums[mid] <= nums[hi]:
                if nums[mid] < target:
                    return bin(mid + 1, hi)
                else:
                    return bin(lo, mid - 1)
            else:
                if nums[mid] > nums[hi]:
                    if nums[lo] <= target < nums[mid]:
                        return bin(lo, mid - 1)
                    else:
                        return bin(mid + 1, hi)
                else:
                    if nums[mid] < target <= nums[hi]:
                        return bin(mid + 1, hi)
                    else:
                        return bin(lo, mid - 1)
        return bin(0, len(nums) - 1)
