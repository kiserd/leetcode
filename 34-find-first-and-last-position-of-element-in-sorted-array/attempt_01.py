# could probably speed things up by breaking function into two separate
# dedicated functions
class Solution:
    def searchRange(self, nums, target: int):
        # get left bound
        res = []
        res.append(self.get_bound(nums, 0, len(nums) - 1, target))
        # handle unsuccessful search
        if res[0] == -1:
            return [-1, -1]
        # get right bound
        res.append(self.get_bound(nums, res[0], len(nums) - 1, target, False))
        return res
    
    def get_bound(self, nums, l, r, target, left=True):
        # handle failure base case
        if l > r:
            return -1
        # handle success base case
        mid = l + ((r - l) // 2)
        if nums[mid] == target:
            # two cases where mid is left bound
            if left:
                if l == mid:
                    return mid
                elif nums[mid - 1] != target:
                    return mid
            # two cases where mid is right bound
            else:
                if r == mid:
                    return mid
                elif nums[mid + 1] != target:
                    return mid
        # handle recursive exploration
        if left:
            if nums[mid] >= target:
                return self.get_bound(nums, l, mid - 1, target)
            else:
                return self.get_bound(nums, mid + 1, r, target)
        else:
            if nums[mid] <= target:
                return self.get_bound(nums, mid + 1, r, target, False)
            else:
                return self.get_bound(nums, l, mid - 1, target, False)