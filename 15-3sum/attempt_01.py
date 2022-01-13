class Solution:
    def threeSum(self, nums):
        res = set()
        # visited = []
        for i in range(len(nums)):
            k = -nums[i]
            helper = {}
            for j in range(i + 1, len(nums), 1):
                # handle case where previous numbers add to zero
                if nums[j] in helper:
                    new = helper[nums[j]]
                    new.append(nums[j])
                    new.sort()
                    res.add(tuple(new))
                    del helper[nums[j]]
                # add new combination to helper dict
                helper[k - nums[j]] = [-k, nums[j]]
                # visited.append(nums[j])
        return list(res)



# for every number processed, we need to know three things:
#   (1) does the current number plus two previous numbers equal 0?
#   (2) does the current number plus two subsequent numbers equal 0?
#   (3) does the current number plus a previous and subsequent number equal 0?

# another way to look at things is that we are looking for i, j, and k s.t.
#   nums[i] + nums[j] + nums[k] == 0 => -nums[i] = nums[j] + nums[k]

# trying to accomplish the above in < O(n^2) or O(n^3)

# maybe try a nested loop with the k-difference problem inside
# for the k-difference problem, at each element i, we need to know two things:
#   (1) does this element less k equal a previous element
#   (2) does a future element less k equal this element

#        0 == nums[i] + nums[j] + nums[k]
# -nums[i] == nums[j] + nums[k]

# ** let k == -nums[i] **

#        k == nums[j] + nums[k]
#  nums[j] == k - nums[k]

