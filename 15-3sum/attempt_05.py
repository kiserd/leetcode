class Solution:
    def threeSum(self, nums):
        # sort array for ease of processing
        nums.sort()
        # process array from left to right
        i = 0
        res = []
        while i < len(nums) - 2 and nums[i] < 1:
            # guard against duplicate results
            if nums[i] != nums[i - 1] or i == 0:
                target = -nums[i]
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    # handle case where sum is too low
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    # handle case where sum is too high
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    # handle "successful" combination
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        k -= 1
                        j += 1
                        # guard against duplicate results
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
            i += 1
        return res
