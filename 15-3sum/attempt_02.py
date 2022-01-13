class Solution:
    def threeSum(self, nums):
        # handle edge cases
        if len(nums) < 3:
            return []
        # first sort the array
        nums.sort()
        # use outer loop to set k
        # stop checking when non-zero negative elements end, can't have
        # non-zero positive elements summing to 0
        i = 0
        res = set()
        visited = []
        # print('nums: ', nums)
        while nums[i] <= 0 and i < len(nums) - 2:
            if nums[i] not in visited:
                k = -nums[i]
                # use two pointer approach to find elements whose sum is k
                # remember nums[i] <= nums[i + 1] <= nums[i + 2]
                m = i + 1
                n = len(nums) - 1
                while m < n: # come back to fix this
                    # handle case of a hit
                    if k == nums[m] + nums[n]:
                        res.add((nums[i], nums[m], nums[n],))
                        m += 1
                        n -= 1
                    # if our two numbers are lower, we adjust the negative num
                    # higher to increase the rhs sum (in equation below)
                    elif nums[m] + nums[n] < k:
                        m += 1
                    # need our sum to be lower
                    else:
                        n -= 1
                # visited.append(nums[i])
            i += 1
        return list(res)



# one approach I had considered was sorting the array prior to processing
# I had assumed this was off limits until taking a peek at the solutions
# after I came up with an initial (naive) solution

# utilize an outer loop that sets our 'k' variable. Then test the following
# elements (using 2-pointer) for:
#   k == -nums[i]
#   k == nums[j] + nums[l]

