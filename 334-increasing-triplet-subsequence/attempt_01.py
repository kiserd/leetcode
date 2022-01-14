import math
class Solution:
    def increasingTriplet(self, nums) -> bool:
        fst = math.inf
        scd = math.inf
        for num in nums:
            if num <= fst:
                fst = num
            elif num <= scd:
                scd = num
            else:
                return True
        return False


# [2, 3, 1, 4, 1, 2] -- example of where greedy reset would break down a bit
# [2, 3, 1, 0, 3]

# only keep track of two numbers, beginning and middle

# [2, 3, 4, 1, 2, 4, 1, 2]

# fst = 2
# scd = inf

# fst = 2
# scd = 3

# fst = 2
# scd = 3

# fst = 1
# scd = 3

# fst = 1
# scd = 2

# returns true

# explanation:
# we only keep track of the first and second smallest
# encountered thus far.

# when we hit the 4, we don't update anything

# when we hit the 1, our second smallest number (3) is not removed or changed.
# we can safely forget our first element of that subsequence. We just need to
# know if a subsequent element is greater than our 3.

# when we hit the second 2, we can safely update scd, because we how have a
# second smallest number that is less than the original (3) and any inc
# subsequence found for our original scd smallest (3) will also return true
# for the new one with 2 as our scd smallest