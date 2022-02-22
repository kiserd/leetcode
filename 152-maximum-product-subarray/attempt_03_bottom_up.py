class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        max_prod = -11
        pos = 0
        neg = 0
        for num in nums:
            temp_neg = neg
            temp_pos = pos
            pos = max(num, num * temp_pos, num * temp_neg)
            neg = min(num, num * temp_pos, num * temp_neg)
            max_prod = max(max_prod, pos)
        return max(max_prod, pos)

# works well for all scenarios. 

# If a negative number hits, the pos running
# product reverts back to zero via num * neg (in the case where no prior neg
# total is being built) OR in the case where negative amount has been building,
# the pos running total flips the sign on the neg running total when
# multiplying with the new number.

# still with a negative number hitting, the neg running total will either
# assume the number that hit OR will flip the sign on the running pos total

# if a positive number hits, pos will either continue building the pos product
# it was working on OR if pos is zero, it will just take num

# if a positive hits, neg will either be zero if there was no neg amount being
# built yet OR build on the negative amount being accumulated

                
            



